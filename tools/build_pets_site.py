from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import tempfile
import time
import unicodedata
import zipfile
from collections import Counter, deque
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "characters.json"
PETS_DIR = ROOT / "pets"
DOCS_DIR = ROOT / "docs"
SOURCE_DIR = DOCS_DIR / "assets" / "source"
OFFICIAL_SITE_DIR = DOCS_DIR / "assets" / "official"
PREVIEW_DIR = DOCS_DIR / "assets" / "previews"
SPRITESHEET_DIR = DOCS_DIR / "assets" / "spritesheets"
DETAIL_SPRITESHEET_DIR = DOCS_DIR / "assets" / "detail-spritesheets"
DOWNLOAD_DIR = DOCS_DIR / "downloads"
DATA_DIR = DOCS_DIR / "data"
ASSET_CACHE_DIR = Path(
    os.environ.get(
        "REVERSE_1999_ASSET_DIR",
        str(ROOT / "assets" / "source-cache" / "Reverse-1999-CN-Asset"),
    )
)
LIVE2D_RENDER_DEPS = Path(os.environ.get("LIVE2D_RENDER_DEPS", str(ROOT / ".deps" / "live2d-render")))
LIVE2D_CUBISM_CORE = Path(os.environ.get("LIVE2D_CUBISM_CORE", str(LIVE2D_RENDER_DEPS / "live2dcubismcore.min.js")))
LIVE2D_RENDER_ENABLED = os.environ.get("NINEPETS_RENDER_LIVE2D", "1") != "0"
LIVE2D_RENDER_SCRIPT = ROOT / "tools" / "render_live2d_frames.mjs"
BUILD_TMP_DIR = ROOT / ".tmp" / "build"
LIVE2D_FRAME_ROOT = ROOT / "assets" / "rendered-frames" / "live2d"
SPINE_RENDER_ENABLED = os.environ.get("NINEPETS_RENDER_SPINE", "1") != "0"
SPINE_RENDER_SCRIPT = ROOT / "tools" / "render_spine_frames.mjs"
SPINE_FRAME_ROOT = ROOT / "assets" / "rendered-frames" / "spine"

CELL_W = 192
CELL_H = 208
COLS = 8
ROWS = 9
DETAIL_ATLAS_SCALE = 4
CUTE_PACKAGE_PREFIX = "9Pets-Cute-"
DEFAULT_SKIN_NAME = "Default"
HIDDEN_NORMAL_CHARACTERS = {
    "Baby Blue",
    "Balloon Party",
}
HIDDEN_NORMAL_PACKAGES = {
    "9Pets-Baby-Blue",
    "9Pets-Baby-Blue-Default",
    "9Pets-Balloon-Party",
    "9Pets-Balloon-Party-Default",
}
NORMAL_SPINE_OVERRIDE_PACKAGES: set[str] = set()
LIVE2D_WHITE_BLOCK_ARTIFACT_PACKAGES = {
    "9Pets-37-A-Gift-of-Nourishment",
    "9Pets-37-A-Prime-Number",
    "9Pets-37-Happy-Bird-Catcher",
    "9Pets-37-Down-in-the-Grotto",
}
CUTE_SPINE_SOURCE_OVERRIDES: dict[str, dict[str, str]] = {
    "9Pets-Cute-A-Knight": {
        "assetId": "300701",
        "spinePath": "roles/300701_weixiukai",
        "skinName": "Official chibi battle model",
    },
    "9Pets-Cute-Coppelia": {
        "assetId": "314401",
        "spinePath": "roles/v3a7_314401_fly",
        "skinName": "Official chibi battle model",
    },
    "9Pets-Cute-Regulus": {
        "assetId": "500501",
        "spinePath": "roles/500501_xingti2hao",
        "skinName": "Official chibi battle model",
    },
    "9Pets-Cute-Sotheby": {
        "assetId": "300901",
        "spinePath": "roles/300901_sufubi",
        "skinName": "Official chibi battle model",
    },
}

LIVE2D_RENDER_PROFILES: dict[str, dict[str, Any]] = {
    "9Pets-6": {
        "width": 1600,
        "height": 1800,
        "scale": 0.72,
        "x": 1000,
        "y": 900,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_qianxun.motion3.json",
            "running-left": "b_qianxun.motion3.json",
            "waving": "b_taishou.motion3.json",
            "jumping": "b_qianxun.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_shalou.motion3.json",
            "running": "b_yuedu.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-6-The-Perfect-Number": {
        "width": 1600,
        "height": 1900,
        "scale": 0.72,
        "x": 1000,
        "y": 900,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_yaotou.motion3.json",
            "running-left": "b_yaotou.motion3.json",
            "waving": "b_taishou.motion3.json",
            "jumping": "b_diantou.motion3.json",
            "failed": "t_nanguo.motion3.json",
            "waiting": "b_diantou.motion3.json",
            "running": "b_yuedu.motion3.json",
            "review": "b_yuedu.motion3.json",
        },
    },
    "9Pets-A-Knight": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_xingli.motion3.json",
            "running-left": "b_xingli.motion3.json",
            "waving": "b_shenshou.motion3.json",
            "jumping": "b_jujian.motion3.json",
            "failed": "b_shengqi.motion3.json",
            "waiting": "b_tanshou.motion3.json",
            "running": "b_cashi.motion3.json",
            "review": "b_sikao.motion3.json",
        },
    },
    "9Pets-Eternity": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_yaotou.motion3.json",
            "running-left": "b_yaotou.motion3.json",
            "waving": "b_baoxiong.motion3.json",
            "jumping": "b_diantou.motion3.json",
            "failed": "t_nanguo.motion3.json",
            "waiting": "b_diantou.motion3.json",
            "running": "b_diantou.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Ezra-Theodore": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_yaotou.motion3.json",
            "running-left": "b_yaotou.motion3.json",
            "waving": "b_jushou.motion3.json",
            "jumping": "b_diantou.motion3.json",
            "failed": "t_nanguo.motion3.json",
            "waiting": "t_yihuo.motion3.json",
            "running": "b_sikao.motion3.json",
            "review": "b_sikao.motion3.json",
        },
    },
    "9Pets-Igor": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_yaotou.motion3.json",
            "running-left": "b_yaotou.motion3.json",
            "waving": "b_tanshou.motion3.json",
            "jumping": "b_diantou.motion3.json",
            "failed": "t_shengqi.motion3.json",
            "waiting": "b_tanshou.motion3.json",
            "running": "b_sikao.motion3.json",
            "review": "b_sikao.motion3.json",
        },
    },
    "9Pets-Aleph": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_touzi2.motion3.json",
            "running-left": "b_touzi2.motion3.json",
            "waving": "b_yanshuo3.motion3.json",
            "jumping": "b_fenlie2.motion3.json",
            "failed": "b_tongku2.motion3.json",
            "waiting": "b_shoushu2.motion3.json",
            "running": "b_yanshuo2.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Alexios": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_cajian.motion3.json",
            "running-left": "b_cajian.motion3.json",
            "waving": "b_tanshou.motion3.json",
            "jumping": "b_woquan.motion3.json",
            "failed": "b_baobi.motion3.json",
            "waiting": "b_yaotou.motion3.json",
            "running": "b_cajian.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-An-an-Lee": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_kaiji.motion3.json",
            "running-left": "b_kaiji.motion3.json",
            "waving": "b_daiyanjing.motion3.json",
            "jumping": "b_kaiji.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_dahaqian.motion3.json",
            "running": "b_sikao.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Anjo-Nala": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_ruchang.motion3.json",
            "running-left": "b_ruchang.motion3.json",
            "waving": "b_fangkai.motion3.json",
            "jumping": "b_huizhua.motion3.json",
            "failed": "b_wuzui.motion3.json",
            "waiting": "b_qidao.motion3.json",
            "running": "b_tanhui.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Argus": {
        "width": 1800,
        "height": 1800,
        "scale": 0.84,
        "x": 1050,
        "y": 560,
        "primaryTexture": "textures/309701_aegs.png",
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_baqiang1.motion3.json",
            "running-left": "b_baqiang2.motion3.json",
            "waving": "b_shenshou1.motion3.json",
            "jumping": "b_baqiang3.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_baoxiong.motion3.json",
            "running": "b_maoyan.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Avgust": {
        "width": 1800,
        "height": 1800,
        "scale": 0.84,
        "x": 1050,
        "y": 560,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_xiangrikui.motion3.json",
            "running-left": "b_diaozhui.motion3.json",
            "waving": "b_shenshou.motion3.json",
            "jumping": "b_xiangrikui.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_waitou.motion3.json",
            "running": "b_diaozhui.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Barbara": {
        "width": 1800,
        "height": 1800,
        "scale": 0.84,
        "x": 1050,
        "y": 560,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_zhaierji.motion3.json",
            "running-left": "b_waitou.motion3.json",
            "waving": "b_zhaierji.motion3.json",
            "jumping": "b_zhaierji.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_fuxiong.motion3.json",
            "running": "b_sikao.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Barcarola": {
        "width": 1800,
        "height": 1800,
        "scale": 0.78,
        "x": 1050,
        "y": 600,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_zhihui.motion3.json",
            "running-left": "b_tanshou.motion3.json",
            "waving": "b_tanshou.motion3.json",
            "jumping": "b_tietie.motion3.json",
            "failed": "b_wuzui.motion3.json",
            "waiting": "b_chayao.motion3.json",
            "running": "b_zhihui.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Beryl": {
        "width": 1800,
        "height": 1800,
        "scale": 0.72,
        "x": 1050,
        "y": 640,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_liyi.motion3.json",
            "running-left": "b_bukan.motion3.json",
            "waving": "b_taishou.motion3.json",
            "jumping": "b_lingbai.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_fuxiong.motion3.json",
            "running": "b_bukan2.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Blonney": {
        "width": 1800,
        "height": 1800,
        "scale": 0.78,
        "x": 1050,
        "y": 900,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_bijiben.motion3.json",
            "running-left": "b_motoufa.motion3.json",
            "waving": "b_motoufa.motion3.json",
            "jumping": "b_yaotou.motion3.json",
            "failed": "t_kongju.motion3.json",
            "waiting": "b_bijiben.motion3.json",
            "running": "b_bijiben.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Brimley": {
        "width": 1800,
        "height": 1800,
        "scale": 0.78,
        "x": 1050,
        "y": 900,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_xingli.motion3.json",
            "running-left": "b_feizou.motion3.json",
            "waving": "b_xingfen.motion3.json",
            "jumping": "b_tiaoyue.motion3.json",
            "failed": "b_shoushang.motion3.json",
            "waiting": "b_shiluo.motion3.json",
            "running": "b_feizou.motion3.json",
            "review": "b_shiluo.motion3.json",
        },
    },
    "9Pets-Brume": {
        "width": 1800,
        "height": 2200,
        "scale": 0.68,
        "x": 1050,
        "y": 760,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_xiaolong.motion3.json",
            "running-left": "b_fue.motion3.json",
            "waving": "b_tanshou.motion3.json",
            "jumping": "b_wuli.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_jinzhang.motion3.json",
            "running": "b_xiaolong.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Nautika-Behind-the-Unknown": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 850,
        "y": 600,
        "detailAtlasScale": 4,
    },
    "9Pets-Nautika-From-Darkness-Light": {
        "width": 1800,
        "height": 1800,
        "scale": 0.48,
        "x": 900,
        "y": 600,
        "detailAtlasScale": 4,
    },
    "9Pets-Pickles-The-Young-Dog-and-The-Sea": {
        "width": 1800,
        "height": 1800,
        "scale": 0.68,
        "x": 850,
        "y": 600,
        "detailAtlasScale": 4,
    },
    "9Pets-Rhiannon-The-Migration-of-Her-Heart": {
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_yaotou.motion3.json",
            "running-left": "b_yaotou.motion3.json",
            "waving": "b_chizhang.motion3.json",
            "jumping": "b_diantou.motion3.json",
            "failed": "t_nanguo.motion3.json",
            "waiting": "t_yihuo.motion3.json",
            "running": "b_sikao.motion3.json",
            "review": "b_sikao.motion3.json",
        },
    },
    "9Pets-Kiperina": {
        "primaryTexture": "textures/311701_kphh.png",
    },
    "9Pets-Liang-Yue-Above-the-Green-Tiles": {
        "x": 950,
        "hiddenDrawables": ["ArtMesh46", "ArtMesh47", "ArtMesh55", "ArtMesh54", "ArtMesh53", "ArtMesh77"],
    },
    "9Pets-Lorelei": {
        "primaryTexture": "textures/309101_luoleilai_00.png",
    },
    "9Pets-Lucy-A-Robot-Is-Born": {
        "hiddenDrawables": [
            "ArtMesh48",
            "ArtMesh49",
            "ArtMesh65",
            "ArtMesh66",
            "ArtMesh67",
            "ArtMesh70",
            "ArtMesh78",
            "ArtMesh80",
            "ArtMesh81",
            "ArtMesh82",
            "ArtMesh83",
        ],
    },
    "9Pets-Buddy-Fairchild": {
        "width": 1800,
        "height": 1800,
        "scale": 0.78,
        "x": 1050,
        "y": 860,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_huiqi1.motion3.json",
            "running-left": "b_huiqi2.motion3.json",
            "waving": "b_zhi1.motion3.json",
            "jumping": "b_wulian.motion3.json",
            "failed": "b_yaotou1.motion3.json",
            "waiting": "b_sikao1.motion3.json",
            "running": "b_sikao2.motion3.json",
            "review": "b_diantou1.motion3.json",
        },
    },
    "9Pets-Charon": {
        "width": 1800,
        "height": 2200,
        "scale": 0.68,
        "x": 1050,
        "y": 760,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_goupai.motion3.json",
            "running-left": "b_fanshu.motion3.json",
            "waving": "b_xianhua.motion3.json",
            "jumping": "b_fanshu3.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_fuxiong.motion3.json",
            "running": "b_goupai.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Cheng-Heguang": {
        "width": 1800,
        "height": 2200,
        "scale": 0.68,
        "x": 1050,
        "y": 760,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_baoquan.motion3.json",
            "running-left": "b_zuanquan.motion3.json",
            "waving": "b_qing.motion3.json",
            "jumping": "b_zuanquan.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_cazui.motion3.json",
            "running": "b_baoquan2.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Click": {
        "width": 1800,
        "height": 1800,
        "scale": 0.84,
        "x": 1050,
        "y": 560,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_xiangji.motion3.json",
            "running-left": "b_paizhao.motion3.json",
            "waving": "b_naotou.motion3.json",
            "jumping": "b_paizhao.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_jiaojuan.motion3.json",
            "running": "b_xiangji.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Coppelia": {
        "width": 1800,
        "height": 2200,
        "scale": 0.68,
        "x": 1050,
        "y": 760,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_yincha.motion3.json",
            "running-left": "b_tanshou.motion3.json",
            "waving": "b_tanshou.motion3.json",
            "jumping": "b_yincha.motion3.json",
            "failed": "b_kuqi.motion3.json",
            "waiting": "b_kuqi1.motion3.json",
            "running": "b_sikao.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-Corvus": {
        "width": 1800,
        "height": 2200,
        "scale": 0.68,
        "x": 1050,
        "y": 760,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_chakan.motion3.json",
            "running-left": "b_chiqiang.motion3.json",
            "waving": "b_taishou.motion3.json",
            "jumping": "b_yamao.motion3.json",
            "failed": "b_yaotou.motion3.json",
            "waiting": "b_zhiweijin_loop.motion3.json",
            "running": "b_chakan_loop.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-37": {
        "width": 1600,
        "height": 1800,
        "scale": 0.75,
        "x": 1000,
        "y": 900,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "b_idle.motion3.json",
            "running-right": "b_tiyi.motion3.json",
            "running-left": "b_tiyi.motion3.json",
            "waving": "b_guzhang.motion3.json",
            "jumping": "b_gongji.motion3.json",
            "failed": "b_xinxu.motion3.json",
            "waiting": "b_zhangshi.motion3.json",
            "running": "b_sisuo.motion3.json",
            "review": "b_diantou.motion3.json",
        },
    },
    "9Pets-37-A-Prime-Number": {
        "width": 1600,
        "height": 1800,
        "scale": 0.75,
        "x": 1000,
        "y": 900,
        "detailAtlasScale": 4,
        "hiddenDrawables": ["bone1", "bone2", "bone3", "bone4"],
    },
    "9Pets-37-Happy-Bird-Catcher": {
        "width": 1600,
        "height": 1800,
        "scale": 0.75,
        "x": 1000,
        "y": 900,
        "detailAtlasScale": 4,
        "hiddenDrawables": ["bone1", "bone2", "bone3", "bone4"],
    },
    "9Pets-37-A-Gift-of-Nourishment": {
        "width": 1600,
        "height": 1800,
        "scale": 0.75,
        "x": 1000,
        "y": 900,
        "detailAtlasScale": 4,
        "hiddenDrawables": ["bone1"],
    },
    "9Pets-37-Down-in-the-Grotto": {
        "width": 2200,
        "height": 2200,
        "scale": 0.60,
        "x": 1450,
        "y": 900,
        "detailAtlasScale": 4,
        "hiddenDrawables": ["bone1", "bone2", "bone3", "bone4", "bone5", "bone6"],
    }
}

SPINE_RENDER_PROFILES: dict[str, dict[str, Any]] = {
    "9Pets-Cute-37": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "306601_37_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "idle_special1",
            "running-left": "idle_special1",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "idle_special1",
        },
    },
    "9Pets-Cute-6": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "307901_6_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Aleph": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "311301_alf_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "channel_idle",
            "review": "unique",
        },
    },
    "9Pets-Cute-A-Knight-Galloping-Across-the-Times": {
        "width": 1600,
        "x": 800,
    },
    "9Pets-Cute-Alexios": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "312201_alkxos_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-aliEn-T": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303401_xingzhiyan_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-An-an-Lee": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303901_nimengdishi_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Anjo-Nala": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "310001_tsnn_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-APPLe": {
        "width": 1600,
        "height": 1600,
        "scale": 2.2,
        "x": 800,
        "y": 1150,
        "skeleton": "302801_apple_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "skill3",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "posture",
        },
    },
    "9Pets-Cute-APPLe-Erudite-and-Juicy": {
        "height": 1900,
        "y": 1350,
    },
    "9Pets-Cute-Argus": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "309701_aegs_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Avgust": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "307801_afuxiwei_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-aliEn-T": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303401_xingzhiyan_fight.skel",
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "idle",
        },
    },
    "9Pets-APPLe": {
        "width": 1600,
        "height": 1600,
        "scale": 2.2,
        "x": 800,
        "y": 1150,
        "skeleton": "302801_apple_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "skill3",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "posture",
        },
    },
    "9Pets-Baby-Blue": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "301601_yingerlan_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "idle_birthday_up",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle_birthday_loop",
            "review": "click",
        },
    },
    "9Pets-Balloon-Party": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "302401_qiqiupaidui_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "walk",
            "failed": "hit",
            "waiting": "sleep",
            "running": "walk",
            "review": "idle",
        },
    },
    "9Pets-Cristallo": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303101_qianboli_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "idle_birthday_up",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle_birthday_loop",
            "review": "click",
        },
    },
    "9Pets-Darley-Clatter": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "305001_dadadali_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "idle_birthday_up",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle_birthday_loop",
            "review": "click",
        },
    },
    "9Pets-Door": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "305901_door_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "walk",
            "failed": "hit",
            "waiting": "sleep",
            "running": "walk",
            "review": "click",
        },
    },
    "9Pets-TTT": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303301_ttt_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "idle",
            "running-left": "idle",
            "waving": "click",
            "jumping": "idle",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle",
            "review": "click",
        },
    },
    "9Pets-Bette": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "304501_beidi_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "idle_birthday_up",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle_birthday_loop",
            "review": "click",
        },
    },
    "9Pets-Bkornblume": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "302001_bolinyidong_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "walk",
            "failed": "hit",
            "waiting": "sleep",
            "running": "walk",
            "review": "click",
        },
    },
    "9Pets-Bunny-Bunny": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "301401_banibani_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "idle_birthday_up",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle_birthday_loop",
            "review": "click",
        },
    },
    "9Pets-Centurion": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303201_baifuzhang_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "idle_birthday_up",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle_birthday_loop",
            "review": "idle_room",
        },
    },
    "9Pets-Charlie": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "301701_xiali_room.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "walk",
            "failed": "hit",
            "waiting": "sleep",
            "running": "walk",
            "review": "idle",
        },
    },
    "9Pets-Cute-Baby-Blue": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "301601_yingerlan_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "victory",
        },
    },
    "9Pets-Cute-Balloon-Party": {
        "width": 1200,
        "height": 1200,
        "scale": 1.8,
        "x": 600,
        "y": 1040,
        "skeleton": "302401_qiqiupaidui_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Barbara": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 980,
        "skeleton": "309901_syg_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Barcarola": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "310801_bkle_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Beryl": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "313401_ble_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill3",
            "review": "unique",
        },
    },
    "9Pets-Cute-Bette": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "304501_beidi_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Bkornblume": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "302001_bolinyidong_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Blonney": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "306001_jinmier_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Charlie": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "301701_xiali_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "victory",
        },
    },
    "9Pets-Cute-Charon": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "312801_kr_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Cheng-Heguang": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "313701_chg_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "channel_idle",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Click": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "304901_kachakacha_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "giddy",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Corvus": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "313201_gsn_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Brimley": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "310601_kym_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "idle",
            "running": "skill1",
            "review": "posture",
        },
    },
    "9Pets-Cute-Brume": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "313501_hdl_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "channel_idle",
            "running": "skill2",
            "review": "channel_idle",
        },
    },
    "9Pets-Cute-Buddy-Fairchild": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "311501_jjsg_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "posture",
        },
    },
    "9Pets-Cute-Bunny-Bunny": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "301401_banibani_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "victory",
        },
    },
    "9Pets-Cute-Centurion": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303201_baifuzhang_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "giddy",
            "waiting": "posture",
            "running": "skill1",
            "review": "posture",
        },
    },
    "9Pets-Cute-Cristallo": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "303101_qianboli_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "skill2",
            "review": "unique",
        },
    },
    "9Pets-Cute-Cristallo-A-Dream-in-Stained-Glass": {
        "y": 1000,
    },
    "9Pets-Cute-Darley-Clatter": {
        "width": 1200,
        "height": 1200,
        "scale": 4.0,
        "x": 600,
        "y": 900,
        "skeleton": "305001_dadadali_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        },
    },
    "9Pets-Cute-Diggers": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "306401_wajueyishu_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "posture",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        },
    },
    "9Pets-Cute-Ezio-Auditore": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "312301_ajaadtl_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "posture",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        },
    },
    "9Pets-Cute-Getian": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "308401_gt_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "posture",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        },
    },
    "9Pets-Cute-Jessica-Voyage-from-your-Bed": {
        "width": 1600,
        "x": 800,
    },
    "9Pets-Cute-Moldir": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "312101_mlde_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "posture",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        },
    },
    "9Pets-Cute-Poltergeist": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "304601_chaonaogui_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "posture",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        },
    },
    "9Pets-Cute-Tennant": {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": "304301_tannante_fight.skel",
        "flipRunningLeft": True,
        "detailAtlasScale": 4,
        "motionMap": {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "posture",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        },
    },
}

STATE_ROWS = [
    ("idle", 6),
    ("running-right", 8),
    ("running-left", 8),
    ("waving", 4),
    ("jumping", 5),
    ("failed", 8),
    ("waiting", 6),
    ("running", 6),
    ("review", 6),
]

OFFICIAL_ROLE_URL = "https://re.bluepoch.com/home/img/role/{asset_id}m.png"
OFFICIAL_THUMB_URL = "https://re.bluepoch.com/home/img/character/{asset_id}.png"
ASSET_REPO_URL = "https://github.com/myssal/Reverse-1999-CN-Asset"
ASSET_RAW_BASE = "https://raw.githubusercontent.com/myssal/Reverse-1999-CN-Asset/master"
ASSET_TREE_BASE = "https://github.com/myssal/Reverse-1999-CN-Asset/tree/master"
ASSET_MAP_URL = f"{ASSET_RAW_BASE}/mappings/ArcanistMap.json"
OFFICIAL_SOURCE_TYPE = "official-sourced"
OFFICIAL_NAME_ALIASES = {
    "37": "Thirty-seven",
    "6": "Six",
    "J": "Joe",
    "Jessica": "Changeling",
    "Kaalaa Baunaa": "Black Dwarf",
    "Liang Yue": "Liang",
    "Matilda": "Matilda Bouanich",
}
OFFICIAL_ENTRY_ID_ALIASES = {
    "Avgust": 3078,
    "Vila": 3087,
    "Zima": 3013,
    "Yenisei": 3082,
}
MANUAL_OFFICIAL_ASSETS = {
    "Avgust": {
        "assetId": 307801,
        "spinePath": "roles/v1a8_307801_afuxiwei",
        "cubismPath": "live2d/roles/v1a8_307801_afuxiwei",
    },
    "Vila": {
        "assetId": 308701,
        "spinePath": "roles/v1a8_308701_weila",
        "cubismPath": "live2d/roles/v1a8_308701_weila",
    },
    "Yenisei": {
        "assetId": 308201,
        "spinePath": "roles/v1a6_308201_xyns",
        "cubismPath": "live2d/roles/v1a6_308201_xiaoyenisai",
    },
    "Zima": {
        "assetId": 301301,
        "spinePath": "roles/301301_dong",
        "cubismPath": "",
    },
}
OFFICIAL_IMAGE_PATHS = [
    "singlebg/headicon_img/{asset_id}.png",
    "singlebg/handbookheroicon/{asset_id}.png",
    "singlebg/handbookheroicon/{asset_id}_1.png",
    "singlebg/handbookheroicon/{asset_id}_2.png",
    "singlebg/data_pic/{asset_id}.png",
    "singlebg/store/skin/{asset_id}.png",
]
OFFICIAL_SITE_ASSETS = {
    "logo.png": "https://re.bluepoch.com/home/img/logo.png",
    "hero-v2.webp": "https://re.bluepoch.com/home/img/v2.webp",
    "hero-v2c.png": "https://re.bluepoch.com/home/img/v2c.png",
    "site-bg.png": "https://re.bluepoch.com/home/img/BG.png",
    "site-bg-2.png": "https://re.bluepoch.com/home/img/BG2.png",
    "main-visual.jpg": "https://re.bluepoch.com/home/img/01.jpg",
    "first-panel-1.png": "https://re.bluepoch.com/home/img/first/1.png",
    "first-panel-2.png": "https://re.bluepoch.com/home/img/first/2.png",
    "first-panel-3.webp": "https://re.bluepoch.com/home/img/first/3.webp",
    "download-panel-3.png": "https://re.bluepoch.com/home/img/first/pc3.png",
    "download-panel-4.png": "https://re.bluepoch.com/home/img/first/pc4.png",
    "news-title.png": "https://re.bluepoch.com/home/img/News.png",
    "see.png": "https://re.bluepoch.com/home/img/see.png",
    "arrow.png": "https://re.bluepoch.com/home/img/jian.png",
    "role-frame.webp": "https://re.bluepoch.com/home/img/role/false.webp",
}


def read_catalog() -> dict[str, Any]:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def slug_suffix(name: str) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    text = text.replace("&", "and")
    tokens = re.findall(r"[A-Za-z0-9]+", text)
    return "-".join(tokens) or "Character"


def clean_skin_name(name: str | None) -> str:
    cleaned = re.sub(r"\s+", " ", (name or "").replace("\xa0", " ")).strip()
    return cleaned or DEFAULT_SKIN_NAME


def is_default_skin_name(name: str | None) -> bool:
    return clean_skin_name(name).casefold() == DEFAULT_SKIN_NAME.casefold()


def skin_name_from_entry(skin: dict[str, Any]) -> str:
    return clean_skin_name(skin.get("characterSkinNameEng"))


def package_name_for(name: str, skin_name: str | None = DEFAULT_SKIN_NAME, *, cute: bool = False) -> str:
    prefix = CUTE_PACKAGE_PREFIX if cute else "9Pets-"
    return f"{prefix}{slug_suffix(name)}-{slug_suffix(clean_skin_name(skin_name))}"


def legacy_package_name_for(name: str, *, cute: bool = False) -> str:
    prefix = CUTE_PACKAGE_PREFIX if cute else "9Pets-"
    return f"{prefix}{slug_suffix(name)}"


def base_profile_package_name(name: str, *, cute: bool = False) -> str:
    return legacy_package_name_for(name, cute=cute)


def package_sort_key(pet: dict[str, Any]) -> tuple[int, str, str]:
    return (
        0 if pet.get("isDefaultSkin", True) else 1,
        str(pet.get("displayName", "")).casefold(),
        str(pet.get("skinName", "")).casefold(),
    )


def slug_lower(name: str) -> str:
    return slug_suffix(name).lower()


def normalized_lookup_name(name: str) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def pet_id_from_package(package_name: str) -> str:
    return package_name.lower()


def crop_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda p: 255 if p > 8 else 0).getbbox()
    if bbox:
        return rgba.crop(bbox)

    bg = Image.new("RGBA", rgba.size, rgba.getpixel((0, 0)))
    diff = ImageChops.difference(rgba, bg)
    bbox = diff.getbbox()
    return rgba.crop(bbox) if bbox else rgba


def squared_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum((a[index] - b[index]) ** 2 for index in range(3))


def remove_edge_background(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    if alpha.getextrema()[0] < 12:
        return rgba

    width, height = rgba.size
    pixels = rgba.load()
    samples: list[tuple[int, int, int]] = []
    for x in range(0, width, 6):
        samples.append(pixels[x, 0][:3])
        samples.append(pixels[x, height - 1][:3])
    for y in range(0, height, 6):
        samples.append(pixels[0, y][:3])
        samples.append(pixels[width - 1, y][:3])

    def quantized(color: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple((channel // 8) * 8 for channel in color)

    background_colors = [color for color, _ in Counter(quantized(color) for color in samples).most_common(8)]
    threshold = 36 * 36

    def is_background(x: int, y: int) -> bool:
        pixel = pixels[x, y]
        if pixel[3] < 12:
            return True
        rgb = pixel[:3]
        return any(squared_distance(rgb, color) <= threshold for color in background_colors)

    queue: deque[tuple[int, int]] = deque()
    visited = bytearray(width * height)

    def enqueue(x: int, y: int) -> None:
        index = y * width + x
        if not visited[index] and is_background(x, y):
            visited[index] = 1
            queue.append((x, y))

    for x in range(width):
        enqueue(x, 0)
        enqueue(x, height - 1)
    for y in range(height):
        enqueue(0, y)
        enqueue(width - 1, y)

    output = rgba.copy()
    output_pixels = output.load()
    while queue:
        x, y = queue.popleft()
        output_pixels[x, y] = (0, 0, 0, 0)
        if x > 0:
            enqueue(x - 1, y)
        if x < width - 1:
            enqueue(x + 1, y)
        if y > 0:
            enqueue(x, y - 1)
        if y < height - 1:
            enqueue(x, y + 1)

    return output


def crop_and_fit(image: Image.Image, max_width: int = 174, max_height: int = 198) -> Image.Image:
    cropped = crop_alpha(remove_edge_background(image))
    scale = min(max_width / cropped.width, max_height / cropped.height, 1.0)
    size = (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale)))
    return cropped.resize(size, Image.Resampling.LANCZOS)


def download_image(url: str, output: Path, referer: str | None = None) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        headers = {"User-Agent": "Mozilla/5.0 9PetsBuilder/2.0"}
        if referer:
            headers["Referer"] = referer
        response = requests.get(url, timeout=20, headers=headers)
        if response.status_code != 200:
            return False
        image = normalize_transparent_pixels(remove_edge_background(Image.open(BytesIO(response.content)).convert("RGBA")))
        for attempt in range(8):
            try:
                image.save(output)
                return True
            except PermissionError:
                if attempt == 7:
                    return False
                time.sleep(0.35)
        return False
    except Exception:
        return False


def download_binary(url: str, output: Path) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, timeout=12, headers={"User-Agent": "Mozilla/5.0 9PetsBuilder/2.0"})
        if response.status_code != 200:
            return False
        output.write_bytes(response.content)
        return True
    except Exception:
        return False


def normalize_transparent_pixels(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    if rgba.getchannel("A").getextrema()[0] > 0:
        return rgba
    clean = Image.new("RGBA", rgba.size, (0, 0, 0, 0))
    clean.alpha_composite(rgba)
    return clean


def source_image_score(image: Image.Image) -> float:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda p: 255 if p > 8 else 0).getbbox()
    if not bbox:
        return -1_000_000

    total = rgba.width * rgba.height
    transparent = sum(1 for value in alpha.getdata() if value <= 8)
    transparent_ratio = transparent / max(total, 1)
    bbox_width = bbox[2] - bbox[0]
    bbox_height = bbox[3] - bbox[1]
    bbox_area = bbox_width * bbox_height
    alpha_min, alpha_max = alpha.getextrema()
    score = min(total / 800, 5_000) + min(bbox_area / 600, 3_000) + transparent_ratio * 2_500
    if alpha_max < 32:
        score -= 5_000
    if alpha_min > 8:
        score -= 8_000
    return score


def save_best_local_source_image(asset_id: int, source_path: Path) -> tuple[str, str] | None:
    candidates: list[tuple[float, str, Image.Image]] = []
    for template in OFFICIAL_IMAGE_PATHS:
        repo_path = template.format(asset_id=asset_id)
        local_path = local_asset_path(repo_path)
        if not local_path.exists():
            continue
        try:
            image = normalize_transparent_pixels(Image.open(local_path).convert("RGBA"))
        except Exception:
            continue
        candidates.append((source_image_score(image), repo_path, image))

    if not candidates:
        return None

    _, repo_path, image = max(candidates, key=lambda item: item[0])
    source_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(source_path)
    return repo_path, repo_raw_url(repo_path)


def download_official_site_assets() -> dict[str, str]:
    assets: dict[str, str] = {}
    for filename, url in OFFICIAL_SITE_ASSETS.items():
        output = OFFICIAL_SITE_DIR / filename
        if download_binary(url, output):
            assets[filename] = url

    for asset_id in range(1, 11):
        filename = f"character-{asset_id}.png"
        url = OFFICIAL_THUMB_URL.format(asset_id=asset_id)
        output = OFFICIAL_SITE_DIR / filename
        if download_binary(url, output):
            assets[filename] = url

    for asset_id in range(1, 11):
        filename = f"role-{asset_id}.png"
        url = OFFICIAL_ROLE_URL.format(asset_id=asset_id)
        output = OFFICIAL_SITE_DIR / filename
        if download_binary(url, output):
            assets[filename] = url

    return assets


def repo_raw_url(path: str) -> str:
    return f"{ASSET_RAW_BASE}/{path}"


def repo_tree_url(path: str) -> str:
    return f"{ASSET_TREE_BASE}/{path}" if path else ""


def repo_path_from_tree_url(url: str) -> str:
    marker = "/tree/master/"
    if marker not in url:
        return ""
    return url.split(marker, 1)[1]


def local_asset_path(repo_path: str) -> Path:
    return ASSET_CACHE_DIR / repo_path if repo_path else Path()


def repo_relative_path(path: Path) -> str:
    return path.relative_to(ASSET_CACHE_DIR).as_posix()


def has_live2d_model(model_dir: Path) -> bool:
    return model_dir.exists() and any(model_dir.glob("*.model3.json"))


def resolve_cached_cubism_path(asset_id: int | str, mapped_path: str) -> str:
    if live2d_model_cached(mapped_path):
        return mapped_path

    asset_key = str(asset_id)
    roles_dir = ASSET_CACHE_DIR / "live2d" / "roles"
    if not roles_dir.exists() or not asset_key:
        return mapped_path

    candidates = [path for path in roles_dir.glob(f"*{asset_key}*") if path.is_dir() and has_live2d_model(path)]
    if not candidates:
        return mapped_path

    def score(path: Path) -> tuple[int, int, str]:
        name = path.name.lower()
        if name.startswith(f"{asset_key}_"):
            rank = 3
        elif f"_{asset_key}_" in name or f"_{asset_key}" in name:
            rank = 2
        else:
            rank = 1
        return (rank, -len(name), name)

    return repo_relative_path(max(candidates, key=score))


def live2d_render_ready(cubism_path: str) -> bool:
    model_dir = local_asset_path(cubism_path)
    return (
        LIVE2D_RENDER_ENABLED
        and bool(cubism_path)
        and has_live2d_model(model_dir)
        and LIVE2D_RENDER_SCRIPT.exists()
        and LIVE2D_RENDER_DEPS.exists()
        and LIVE2D_CUBISM_CORE.exists()
    )


def live2d_model_cached(cubism_path: str) -> bool:
    model_dir = local_asset_path(cubism_path)
    return bool(cubism_path) and has_live2d_model(model_dir)


def write_temp_json(payload: Any, prefix: str) -> Path:
    BUILD_TMP_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        prefix=prefix,
        suffix=".json",
        delete=False,
        encoding="utf-8",
        dir=BUILD_TMP_DIR,
    ) as handle:
        json.dump(payload, handle)
        return Path(handle.name)


def is_default_skin(skin: dict[str, Any]) -> bool:
    return is_default_skin_name(skin.get("characterSkinNameEng"))


def default_spine_render_profile(package_name: str, spine_path: str) -> dict[str, Any]:
    spine_dir = local_asset_path(spine_path)
    if not spine_dir.exists():
        return {}
    is_cute = package_name.startswith(CUTE_PACKAGE_PREFIX)
    skeleton_pattern = "*_fight.skel" if is_cute else "*_room.skel"
    skeletons = sorted(spine_dir.glob(skeleton_pattern))
    if not skeletons:
        return {}
    asset_match = re.search(r"(\d{6})", spine_dir.name)
    asset_key = asset_match.group(1) if asset_match else ""

    def score_asset_file(path: Path) -> tuple[int, int, str]:
        stem = path.stem.lower()
        rank = 1
        if asset_key and stem.startswith(asset_key):
            rank = 3
        elif asset_key and asset_key in stem:
            rank = 2
        return (rank, -len(path.name), path.name.lower())

    skeleton = max(skeletons, key=score_asset_file)
    skeleton_base = re.sub(r"_(fight|room|ui)(?:_special)?$", "", skeleton.stem, flags=re.IGNORECASE)
    atlases = sorted(spine_dir.glob("*.atlas"))
    atlas = next((path for path in atlases if path.stem.casefold() == skeleton_base.casefold()), None)
    if atlas is None and atlases:
        atlas = max(atlases, key=score_asset_file)
    profile: dict[str, Any] = {
        "width": 1200,
        "height": 1200,
        "scale": 2.2,
        "x": 600,
        "y": 900,
        "skeleton": skeleton.name,
        "flipRunningLeft": True,
        "detailAtlasScale": DETAIL_ATLAS_SCALE,
    }
    if atlas:
        profile["atlas"] = atlas.name
    if is_cute:
        profile["motionMap"] = {
            "idle": "idle",
            "running-right": "posture",
            "running-left": "posture",
            "waving": "giddy",
            "jumping": "skill1",
            "failed": "hit",
            "waiting": "sleep",
            "running": "posture",
            "review": "posture",
        }
    else:
        profile["motionMap"] = {
            "idle": "idle",
            "running-right": "walk",
            "running-left": "walk",
            "waving": "click",
            "jumping": "idle_birthday_up",
            "failed": "hit",
            "waiting": "sleep",
            "running": "idle_birthday_loop",
            "review": "click",
        }
    return profile


def inherit_layout_profile(profile: dict[str, Any], *, drop_keys: set[str]) -> dict[str, Any]:
    return {key: value for key, value in profile.items() if key not in drop_keys}


def live2d_render_profile_for(package_name: str, profile_package_name: str | None = None) -> dict[str, Any]:
    exact = LIVE2D_RENDER_PROFILES.get(package_name)
    if exact:
        return dict(exact)
    inherited = LIVE2D_RENDER_PROFILES.get(profile_package_name) if profile_package_name else None
    if inherited:
        return inherit_layout_profile(dict(inherited), drop_keys={"motionMap", "primaryTexture"})
    return {}


def spine_render_profile_for(package_name: str, spine_path: str, profile_package_name: str | None = None) -> dict[str, Any]:
    exact = SPINE_RENDER_PROFILES.get(package_name)
    if exact:
        profile = default_spine_render_profile(package_name, spine_path)
        inherited = SPINE_RENDER_PROFILES.get(profile_package_name) if profile_package_name else None
        if inherited:
            profile.update(inherit_layout_profile(dict(inherited), drop_keys={"skeleton", "atlas"}))
        profile.update(dict(exact))
        return profile
    inherited = SPINE_RENDER_PROFILES.get(profile_package_name) if profile_package_name else None
    if inherited:
        profile = default_spine_render_profile(package_name, spine_path)
        profile.update(inherit_layout_profile(dict(inherited), drop_keys={"skeleton", "atlas"}))
        return profile
    return default_spine_render_profile(package_name, spine_path)


def spine_render_ready(package_name: str, spine_path: str, profile_package_name: str | None = None) -> bool:
    spine_dir = local_asset_path(spine_path)
    profile = spine_render_profile_for(package_name, spine_path, profile_package_name)
    return (
        SPINE_RENDER_ENABLED
        and bool(profile)
        and bool(spine_path)
        and spine_dir.exists()
        and any(spine_dir.glob("*.skel"))
        and any(spine_dir.glob("*.atlas"))
        and SPINE_RENDER_SCRIPT.exists()
        and LIVE2D_RENDER_DEPS.exists()
    )


def render_live2d_frames(package_name: str, cubism_path: str, profile_package_name: str | None = None) -> Path | None:
    if not live2d_render_ready(cubism_path):
        return None

    profile = live2d_render_profile_for(package_name, profile_package_name)
    output_dir = LIVE2D_FRAME_ROOT / package_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    model_dir = local_asset_path(cubism_path)
    command = [
        "node",
        str(LIVE2D_RENDER_SCRIPT),
        "--model-dir",
        str(model_dir),
        "--output",
        str(output_dir),
        "--deps-dir",
        str(LIVE2D_RENDER_DEPS),
        "--cubism-core",
        str(LIVE2D_CUBISM_CORE),
        "--width",
        str(profile.get("width", 1800)),
        "--height",
        str(profile.get("height", 1800)),
        "--scale",
        str(profile.get("scale", 0.68)),
        "--x",
        str(profile.get("x", 1050)),
        "--y",
        str(profile.get("y", 600)),
    ]
    if profile.get("primaryTexture"):
        command.extend(["--primary-texture", str(profile["primaryTexture"])])
    if profile.get("hiddenDrawables"):
        command.extend(["--hidden-drawables", ",".join(str(item) for item in profile["hiddenDrawables"])])
    motion_map_path: Path | None = None
    try:
        if profile.get("motionMap"):
            motion_map_path = write_temp_json(profile["motionMap"], f"{package_name}-live2d-motion-")
            command.extend(["--motion-map", str(motion_map_path)])
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=240, check=False)
        if completed.returncode != 0:
            print(f"Live2D render failed for {package_name}: {completed.stderr.strip() or completed.stdout.strip()}", flush=True)
            return None
        if completed.stdout.strip():
            print(completed.stdout.strip(), flush=True)
        return output_dir
    finally:
        if motion_map_path:
            motion_map_path.unlink(missing_ok=True)


def render_spine_frames(package_name: str, spine_path: str, profile_package_name: str | None = None) -> Path | None:
    if not spine_render_ready(package_name, spine_path, profile_package_name):
        return None

    profile = spine_render_profile_for(package_name, spine_path, profile_package_name)
    output_dir = SPINE_FRAME_ROOT / package_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    spine_dir = local_asset_path(spine_path)
    command = [
        "node",
        str(SPINE_RENDER_SCRIPT),
        "--spine-dir",
        str(spine_dir),
        "--output",
        str(output_dir),
        "--deps-dir",
        str(LIVE2D_RENDER_DEPS),
        "--width",
        str(profile.get("width", 1200)),
        "--height",
        str(profile.get("height", 1200)),
        "--scale",
        str(profile.get("scale", 1)),
        "--x",
        str(profile.get("x", 600)),
        "--y",
        str(profile.get("y", 900)),
    ]
    if profile.get("flipRunningLeft"):
        command.append("--flip-running-left")
    if profile.get("skeleton"):
        command.extend(["--skeleton", str(profile["skeleton"])])
    if profile.get("atlas"):
        command.extend(["--atlas", str(profile["atlas"])])
    motion_map_path: Path | None = None
    try:
        if profile.get("motionMap"):
            motion_map_path = write_temp_json(profile["motionMap"], f"{package_name}-spine-motion-")
            command.extend(["--motion-map", str(motion_map_path)])
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=240, check=False)
        if completed.returncode != 0:
            print(f"Spine render failed for {package_name}: {completed.stderr.strip() or completed.stdout.strip()}", flush=True)
            return None
        if completed.stdout.strip():
            print(completed.stdout.strip(), flush=True)
        return output_dir
    finally:
        if motion_map_path:
            motion_map_path.unlink(missing_ok=True)


def load_official_asset_index() -> dict[str, dict[str, Any]]:
    local_map = ASSET_CACHE_DIR / "mappings" / "ArcanistMap.json"
    if local_map.exists():
        entries = json.loads(local_map.read_text(encoding="utf-8"))
    else:
        response = requests.get(ASSET_MAP_URL, timeout=30, headers={"User-Agent": "Mozilla/5.0 9PetsBuilder/2.0"})
        if response.status_code != 200:
            raise RuntimeError(f"Could not download official asset mapping: HTTP {response.status_code}")
        local_map.parent.mkdir(parents=True, exist_ok=True)
        local_map.write_text(response.text, encoding="utf-8")
        entries = response.json()
    index: dict[str, dict[str, Any]] = {}
    for entry in entries:
        keys = {
            normalized_lookup_name(entry.get("nameEng", "")),
            normalized_lookup_name(entry.get("name", "")),
            f"id:{entry.get('id')}",
        }
        for key in keys:
            if key:
                index[key] = entry
    return index


def find_official_entry(name: str, official_index: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    entry_id = OFFICIAL_ENTRY_ID_ALIASES.get(name)
    if entry_id:
        entry = official_index.get(f"id:{entry_id}")
        if entry:
            return entry

    lookup_name = OFFICIAL_NAME_ALIASES.get(name, name)
    return official_index.get(normalized_lookup_name(lookup_name))


def official_skin_entries(name: str, official_index: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    manual = MANUAL_OFFICIAL_ASSETS.get(name)
    entry = find_official_entry(name, official_index)
    if entry and entry.get("live2d"):
        return list(entry["live2d"])
    if manual:
        return [
            {
                "id": manual["assetId"],
                "nameEng": name,
                "characterSkinNameEng": DEFAULT_SKIN_NAME,
                "spine": repo_tree_url(manual.get("spinePath", "")),
                "cubism": repo_tree_url(manual.get("cubismPath", "")),
            }
        ]
    return []


def default_skin_entry(skins: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not skins:
        return None
    return next((candidate for candidate in skins if is_default_skin(candidate)), skins[0])


def resolve_official_asset(
    name: str,
    official_index: dict[str, dict[str, Any]],
    skin_entry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    manual = MANUAL_OFFICIAL_ASSETS.get(name)
    if manual and skin_entry is None and not find_official_entry(name, official_index):
        asset_id = manual["assetId"]
        cubism_path = resolve_cached_cubism_path(asset_id, manual.get("cubismPath", ""))
        return {
            "assetId": asset_id,
            "spinePath": manual.get("spinePath", ""),
            "cubismPath": cubism_path,
            "matchedName": name,
            "birthday": "",
            "skinName": DEFAULT_SKIN_NAME,
            "isDefaultSkin": True,
        }

    lookup_name = OFFICIAL_NAME_ALIASES.get(name, name)
    entry = find_official_entry(name, official_index)
    skins = official_skin_entries(name, official_index)
    if not entry and not skins:
        raise RuntimeError(f"No official asset mapping found for {name}")

    prepared_skins: list[tuple[dict[str, Any], str, str]] = []
    for candidate_skin in skins:
        asset_id = candidate_skin["id"]
        spine_path = repo_path_from_tree_url(candidate_skin.get("spine", ""))
        mapped_cubism_path = repo_path_from_tree_url(candidate_skin.get("cubism", ""))
        cubism_path = resolve_cached_cubism_path(asset_id, mapped_cubism_path)
        prepared_skins.append((candidate_skin, spine_path, cubism_path))

    selected_skin = skin_entry or default_skin_entry(skins)
    selected_id = str(selected_skin["id"]) if selected_skin else ""
    skin, spine_path, cubism_path = next((candidate for candidate in prepared_skins if str(candidate[0]["id"]) == selected_id), prepared_skins[0])
    skin_name = skin_name_from_entry(skin)
    return {
        "assetId": skin["id"],
        "spinePath": spine_path,
        "cubismPath": cubism_path,
        "matchedName": lookup_name,
        "birthday": entry.get("roleBirthday", "") if entry else "",
        "skinName": skin_name,
        "isDefaultSkin": is_default_skin_name(skin_name),
        "skinDescription": skin.get("skinDescription", ""),
    }


def download_official_source_image(asset_id: int, source_path: Path) -> tuple[str, str]:
    local_source = save_best_local_source_image(asset_id, source_path)
    if local_source:
        return local_source

    for template in OFFICIAL_IMAGE_PATHS:
        repo_path = template.format(asset_id=asset_id)
        local_path = local_asset_path(repo_path)
        if not local_path.exists():
            download_image(repo_raw_url(repo_path), local_path)

    local_source = save_best_local_source_image(asset_id, source_path)
    if local_source:
        return local_source

    if source_path.exists():
        return source_path.relative_to(DOCS_DIR).as_posix(), ""
    raise RuntimeError(f"No official source image found for asset id {asset_id}")


def get_source_sprite(
    name: str,
    package_name: str,
    official_index: dict[str, dict[str, Any]],
    skin_entry: dict[str, Any] | None = None,
) -> tuple[Image.Image, dict[str, Any]]:
    asset = resolve_official_asset(name, official_index, skin_entry)
    source_path = SOURCE_DIR / f"{package_name}.png"
    image_repo_path, source_url = download_official_source_image(int(asset["assetId"]), source_path)
    sprite = crop_and_fit(Image.open(source_path).convert("RGBA"), max_width=180, max_height=200)
    cubism_path = asset.get("cubismPath", "")
    spine_path = asset.get("spinePath", "")
    source_info = {
        "sourceType": OFFICIAL_SOURCE_TYPE,
        "sourceUrl": source_url,
        "sourceImage": f"assets/source/{package_name}.png",
        "sourceRepoPath": image_repo_path,
        "assetId": str(asset["assetId"]),
        "assetRepoUrl": ASSET_REPO_URL,
        "spinePath": spine_path,
        "cubismPath": cubism_path,
        "spineUrl": repo_tree_url(spine_path),
        "cubismUrl": repo_tree_url(cubism_path),
        "birthday": asset.get("birthday", ""),
        "skinName": asset.get("skinName", "Default"),
        "isDefaultSkin": bool(asset.get("isDefaultSkin")),
        "skinDescription": asset.get("skinDescription", ""),
        "matchedName": asset.get("matchedName", name),
        "live2dCacheStatus": "cached" if live2d_model_cached(cubism_path) else ("mapped" if cubism_path else "none"),
        "animationMode": "official-art-elastic-rig",
        "animationModeLabel": "Official art atlas; Live2D path mapped",
    }
    return sprite, source_info


def transformed(
    sprite: Image.Image,
    *,
    scale: float = 1.0,
    scale_x: float = 1.0,
    scale_y: float = 1.0,
    angle: float = 0.0,
    flip: bool = False,
    opacity: float = 1.0,
) -> Image.Image:
    image = sprite
    if flip:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    width_scale = scale * scale_x
    height_scale = scale * scale_y
    if width_scale != 1.0 or height_scale != 1.0:
        size = (max(1, round(image.width * width_scale)), max(1, round(image.height * height_scale)))
        image = image.resize(size, Image.Resampling.LANCZOS)
    if angle:
        image = image.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    if opacity < 1.0:
        alpha = image.getchannel("A").point(lambda p: round(p * opacity))
        image = image.copy()
        image.putalpha(alpha)
    return image


def frame_motion(state: str, frame: int, total: int) -> dict[str, Any]:
    phase = frame / max(total, 1)
    wave = math.sin(phase * math.tau)
    if state == "idle":
        return {"scale_x": 1.0 - 0.01 * abs(wave), "scale_y": 1.0 + 0.018 * abs(wave), "angle": 1.8 * wave, "x": 0, "y": round(-4 * abs(wave)), "flip": False}
    if state == "running-right":
        return {"scale_x": [1.04, 1.0, 0.98, 1.03, 1.06, 1.0, 0.97, 1.02][frame], "scale_y": [0.96, 1.02, 1.04, 0.98, 0.95, 1.03, 1.04, 0.99][frame], "angle": [-8, -3, 4, 8, 3, -5, -9, -2][frame], "x": [-17, -11, -4, 5, 13, 17, 8, -6][frame], "y": [4, -4, -2, -6, 2, -5, -1, 3][frame], "flip": False}
    if state == "running-left":
        return {"scale_x": [1.04, 1.0, 0.98, 1.03, 1.06, 1.0, 0.97, 1.02][frame], "scale_y": [0.96, 1.02, 1.04, 0.98, 0.95, 1.03, 1.04, 0.99][frame], "angle": [8, 3, -4, -8, -3, 5, 9, 2][frame], "x": [17, 11, 4, -5, -13, -17, -8, 6][frame], "y": [4, -4, -2, -6, 2, -5, -1, 3][frame], "flip": True}
    if state == "waving":
        return {"scale_x": [1.0, 0.98, 1.02, 1.0][frame], "scale_y": [1.0, 1.03, 0.99, 1.0][frame], "angle": [0, -12, 11, 2][frame], "x": [0, -6, 6, 1][frame], "y": [0, -8, -5, 0][frame], "flip": False}
    if state == "jumping":
        return {"scale_x": [1.08, 0.98, 0.95, 0.99, 1.06][frame], "scale_y": [0.91, 1.05, 1.09, 1.03, 0.94][frame], "angle": [0, -6, 3, 6, -2][frame], "x": [0, -3, 1, 4, 0][frame], "y": [10, -20, -42, -18, 6][frame], "flip": False}
    if state == "failed":
        return {"scale_x": [1.0, 1.03, 1.08, 1.05, 1.1, 1.07, 1.03, 1.0][frame], "scale_y": [1.0, 0.96, 0.89, 0.92, 0.86, 0.9, 0.95, 1.0][frame], "angle": [0, 9, -8, 13, -12, 8, -4, 0][frame], "x": [0, 3, -5, 5, -6, 4, -2, 0][frame], "y": [8, 14, 22, 18, 25, 20, 14, 8][frame], "flip": False, "opacity": [1, 0.95, 0.9, 0.94, 0.88, 0.92, 0.97, 1][frame]}
    if state == "waiting":
        return {"scale_x": [1.0, 0.99, 0.98, 1.02, 1.01, 1.0][frame], "scale_y": [1.0, 1.02, 1.04, 1.01, 0.99, 1.0][frame], "angle": [0, -4, -7, 6, 3, 0][frame], "x": [0, -3, -5, 4, 2, 0][frame], "y": [0, -4, -8, -5, -2, 1][frame], "flip": False}
    if state == "running":
        return {"scale_x": [1.0, 1.02, 0.98, 1.03, 0.99, 1.0][frame], "scale_y": [1.0, 0.98, 1.04, 0.97, 1.03, 1.0][frame], "angle": [0, -5, 4, -4, 5, 0][frame], "x": [0, -4, 3, -3, 4, 0][frame], "y": [-1, -7, -2, -8, -3, -1][frame], "flip": False}
    if state == "review":
        return {"scale_x": [1.0, 1.01, 1.02, 1.01, 0.99, 1.0][frame], "scale_y": [1.0, 1.02, 1.03, 1.02, 1.0, 0.99][frame], "angle": [0, -4, -6, -3, 1, 0][frame], "x": [0, -4, -7, -4, 1, 0][frame], "y": [0, -3, -6, -3, 0, 1][frame], "flip": False}
    return {"scale": 1.0, "angle": 0, "x": 0, "y": 0, "flip": False}


def alpha_composite_clipped(target: Image.Image, source: Image.Image, pos: tuple[int, int]) -> None:
    x, y = pos
    src_x0 = max(0, -x)
    src_y0 = max(0, -y)
    src_x1 = min(source.width, target.width - x)
    src_y1 = min(source.height, target.height - y)
    if src_x1 <= src_x0 or src_y1 <= src_y0:
        return
    crop = source.crop((src_x0, src_y0, src_x1, src_y1))
    target.alpha_composite(crop, (max(x, 0), max(y, 0)))


def make_cell(sprite: Image.Image, state: str, frame: int, total: int) -> Image.Image:
    motion = frame_motion(state, frame, total)
    image = transformed(
        sprite,
        scale=motion.get("scale", 1.0),
        scale_x=motion.get("scale_x", 1.0),
        scale_y=motion.get("scale_y", 1.0),
        angle=motion.get("angle", 0.0),
        flip=motion.get("flip", False),
        opacity=motion.get("opacity", 1.0),
    )
    margin = 2
    max_width = CELL_W - margin * 2
    max_height = CELL_H - margin * 2
    if image.width > max_width or image.height > max_height:
        scale = min(max_width / image.width, max_height / image.height)
        size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
        image = image.resize(size, Image.Resampling.LANCZOS)
    cell = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
    x = round((CELL_W - image.width) / 2 + motion.get("x", 0))
    y = round(CELL_H - image.height - 8 + motion.get("y", 0))
    x = min(max(x, margin), max(margin, CELL_W - image.width - margin))
    y = min(max(y, margin), max(margin, CELL_H - image.height - margin))
    alpha_composite_clipped(cell, image, (x, y))
    return cell


def make_atlas(sprite: Image.Image) -> Image.Image:
    atlas = Image.new("RGBA", (CELL_W * COLS, CELL_H * ROWS), (0, 0, 0, 0))
    for row, (state, frames) in enumerate(STATE_ROWS):
        for col in range(frames):
            cell = make_cell(sprite, state, col, frames)
            atlas.alpha_composite(cell, (col * CELL_W, row * CELL_H))
    return atlas


def union_bbox(a: tuple[int, int, int, int] | None, b: tuple[int, int, int, int] | None) -> tuple[int, int, int, int] | None:
    if not a:
        return b
    if not b:
        return a
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


def make_live2d_cell(
    frame: Image.Image,
    bbox: tuple[int, int, int, int],
    scale: float,
    *,
    flip: bool = False,
    cell_w: int = CELL_W,
    cell_h: int = CELL_H,
) -> Image.Image:
    image = frame.convert("RGBA").crop(bbox)
    if flip:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    image = image.resize(size, Image.Resampling.LANCZOS)
    cell = Image.new("RGBA", (cell_w, cell_h), (0, 0, 0, 0))
    x = round((cell_w - image.width) / 2)
    y = round(cell_h - image.height - max(6, round(6 * cell_h / CELL_H)))
    alpha_composite_clipped(cell, image, (x, y))
    return cell


def remove_compact_white_block_artifacts(image: Image.Image, package_name: str) -> Image.Image:
    rgba = image.convert("RGBA")
    atlas_scale = max(1, rgba.width // CELL_W)
    min_area = 8 * atlas_scale * atlas_scale
    max_area = 500 * atlas_scale * atlas_scale
    min_size = 3 * atlas_scale
    max_size = 30 * atlas_scale
    pixels = rgba.load()
    candidates: set[tuple[int, int]] = set()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = pixels[x, y]
            if a >= 245 and r >= 248 and g >= 248 and b >= 248 and max(r, g, b) - min(r, g, b) <= 4:
                candidates.add((x, y))

    boxes: list[tuple[int, int, int, int]] = []
    while candidates:
        start = candidates.pop()
        stack = [start]
        xs: list[int] = []
        ys: list[int] = []
        while stack:
            x, y = stack.pop()
            xs.append(x)
            ys.append(y)
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (nx, ny) in candidates:
                    candidates.remove((nx, ny))
                    stack.append((nx, ny))
        area = len(xs)
        left, top, right, bottom = min(xs), min(ys), max(xs) + 1, max(ys) + 1
        width = right - left
        height = bottom - top
        fill = area / (width * height)
        squareish = 0.65 <= width / height <= 1.55
        pad = max(4, round(max(width, height) * 0.75))
        outer = (
            max(0, left - pad),
            max(0, top - pad),
            min(rgba.width, right + pad),
            min(rgba.height, bottom + pad),
        )
        ring_area = 0
        ring_visible = 0
        for ring_y in range(outer[1], outer[3]):
            for ring_x in range(outer[0], outer[2]):
                if left <= ring_x < right and top <= ring_y < bottom:
                    continue
                ring_area += 1
                if pixels[ring_x, ring_y][3] > 32:
                    ring_visible += 1
        isolated = ring_area > 0 and ring_visible / ring_area < 0.16
        solid_square = fill > 0.98 and max(width, height) <= 12 * atlas_scale
        if (
            min_area <= area <= max_area
            and min_size <= width <= max_size
            and min_size <= height <= max_size
            and fill > 0.75
            and squareish
            and (isolated or solid_square)
        ):
            pad_clear = max(1, atlas_scale)
            boxes.append(
                (
                    max(0, left - pad_clear),
                    max(0, top - pad_clear),
                    min(rgba.width, right + pad_clear),
                    min(rgba.height, bottom + pad_clear),
                )
            )

    if not boxes:
        return rgba

    clean = rgba.copy()
    clean_pixels = clean.load()
    for left, top, right, bottom in boxes:
        for y in range(top, bottom):
            for x in range(left, right):
                r, g, b, a = clean_pixels[x, y]
                if a > 0 and r >= 220 and g >= 220 and b >= 220 and max(r, g, b) - min(r, g, b) <= 18:
                    clean_pixels[x, y] = (0, 0, 0, 0)
    return normalize_transparent_pixels(clean)


def make_atlas_from_live2d_frames(frames_root: Path, cell_scale: int = 1) -> Image.Image:
    cell_w = CELL_W * cell_scale
    cell_h = CELL_H * cell_scale
    package_name = frames_root.name
    loaded: dict[str, list[Image.Image]] = {}
    bbox: tuple[int, int, int, int] | None = None
    for state, frame_count in STATE_ROWS:
        state_dir = frames_root / state
        frames: list[Image.Image] = []
        for index in range(frame_count):
            frame_path = state_dir / f"{index:02d}.png"
            if not frame_path.exists():
                raise RuntimeError(f"Missing Live2D frame {frame_path}")
            frame = Image.open(frame_path).convert("RGBA")
            frames.append(frame)
            bbox = union_bbox(bbox, frame.getchannel("A").getbbox())
        loaded[state] = frames

    if not bbox:
        raise RuntimeError(f"Live2D frames are empty under {frames_root}")
    bbox_width = max(1, bbox[2] - bbox[0])
    bbox_height = max(1, bbox[3] - bbox[1])
    scale = min((cell_w - 14 * cell_scale) / bbox_width, (cell_h - 10 * cell_scale) / bbox_height, 1.0)
    atlas = Image.new("RGBA", (cell_w * COLS, cell_h * ROWS), (0, 0, 0, 0))
    for row, (state, frame_count) in enumerate(STATE_ROWS):
        for col in range(frame_count):
            cell = make_live2d_cell(
                loaded[state][col],
                bbox,
                scale,
                flip=state == "running-left",
                cell_w=cell_w,
                cell_h=cell_h,
            )
            cell = remove_compact_white_block_artifacts(cell, package_name)
            atlas.alpha_composite(cell, (col * cell_w, row * cell_h))
    return atlas


def make_preview_from_atlas(atlas: Image.Image, output: Path) -> None:
    preview = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
    preview.alpha_composite(atlas.crop((0, 0, CELL_W, CELL_H)))
    save_image_atomic(preview, output)


def save_image_atomic(image: Image.Image, output: Path, **save_kwargs: Any) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        prefix=f".{output.stem}-",
        suffix=output.suffix,
        dir=output.parent,
        delete=False,
    ) as handle:
        temp_path = Path(handle.name)
    try:
        image.save(temp_path, **save_kwargs)
        temp_path.replace(output)
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def make_pet_json(package_name: str, name: str, source_info: dict[str, Any]) -> dict[str, str]:
    is_cute = package_name.startswith(CUTE_PACKAGE_PREFIX)
    skin_name = clean_skin_name(source_info.get("skinName"))
    display_skin = f" - {skin_name}" if skin_name else ""
    if source_info.get("animationMode") == "official-live2d-cubism":
        description = f"An official-sourced Reverse: 1999 Codex pet for {name} ({skin_name}), built from official Live2D Cubism motion frames."
    elif source_info.get("animationMode") == "official-spine":
        description = f"An official-sourced Reverse: 1999 Codex pet for {name} ({skin_name}), built from official Spine motion frames."
    elif source_info.get("animationMode") == "official-cute-spine":
        description = f"An official-sourced Reverse: 1999 Codex pet cute variant for {name} ({skin_name}), built from official chibi Spine motion frames."
    else:
        description = f"An official-sourced Reverse: 1999 Codex pet for {name} ({skin_name}), built from official game asset-dump artwork."
    return {
        "id": pet_id_from_package(package_name),
        "displayName": f"9Pets Cute - {name}{display_skin}" if is_cute else f"9Pets - {name}{display_skin}",
        "description": description,
        "spritesheetPath": "spritesheet.webp",
    }


def write_zip(package_name: str, pet_json: dict[str, str], spritesheet_path: Path, zip_path: Path, source_info: dict[str, Any]) -> int:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    readme = "\n".join(
        [
            f"# {package_name}",
            "",
            "Official-sourced Codex pet package for Reverse: 1999.",
            f"Source mode: {source_info['sourceType']}.",
            f"Animation mode: {source_info.get('animationModeLabel', source_info.get('animationMode', 'Unknown'))}.",
            f"Official asset id: {source_info['assetId']}.",
            f"Skin: {source_info.get('skinName', DEFAULT_SKIN_NAME)}.",
            f"Source image: {source_info['sourceUrl']}.",
            f"Spine assets: {source_info['spineUrl'] or 'No mapped Spine path.'}",
            f"Live2D assets: {source_info['cubismUrl'] or 'No mapped Live2D path.'}",
            "",
            "Install by copying the package folder contents into your Codex pets directory.",
            "",
        ]
    )
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        prefix = package_name
        archive.writestr(f"{prefix}/pet.json", json.dumps(pet_json, indent=2, ensure_ascii=False) + "\n")
        archive.write(spritesheet_path, f"{prefix}/spritesheet.webp")
        archive.writestr(f"{prefix}/README.md", readme)
    return zip_path.stat().st_size


def clean_output_dirs() -> None:
    output_paths = [PETS_DIR, SOURCE_DIR, OFFICIAL_SITE_DIR, PREVIEW_DIR, SPRITESHEET_DIR, DETAIL_SPRITESHEET_DIR, DOWNLOAD_DIR, DATA_DIR]
    for path in output_paths:
        if path.exists():
            for attempt in range(8):
                try:
                    shutil.rmtree(path)
                    break
                except PermissionError:
                    if attempt == 7:
                        print(f"Warning: could not fully clean locked output path {path}; overwriting build outputs in place.", flush=True)
                    else:
                        time.sleep(0.35)
    for path in output_paths:
        path.mkdir(parents=True, exist_ok=True)


def snapshot_cute_outputs() -> Path | None:
    BUILD_TMP_DIR.mkdir(parents=True, exist_ok=True)
    snapshot_root = Path(tempfile.mkdtemp(prefix="9pets-cute-preserve-", dir=BUILD_TMP_DIR))
    found = False

    for package_dir in PETS_DIR.glob(f"{CUTE_PACKAGE_PREFIX}*"):
        if package_dir.is_dir():
            destination = snapshot_root / "pets" / package_dir.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(package_dir, destination)
            found = True

    for source_dir, pattern in [
        (SOURCE_DIR, f"{CUTE_PACKAGE_PREFIX}*.png"),
        (SPRITESHEET_DIR, f"{CUTE_PACKAGE_PREFIX}*.webp"),
        (DETAIL_SPRITESHEET_DIR, f"{CUTE_PACKAGE_PREFIX}*.webp"),
        (PREVIEW_DIR, f"{CUTE_PACKAGE_PREFIX}*.png"),
        (DOWNLOAD_DIR, f"{CUTE_PACKAGE_PREFIX}*.zip"),
    ]:
        for source_file in source_dir.glob(pattern):
            destination = snapshot_root / source_file.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, destination)
            found = True

    if not found:
        shutil.rmtree(snapshot_root, ignore_errors=True)
        return None
    return snapshot_root


def restore_cute_outputs(snapshot_root: Path | None) -> None:
    if not snapshot_root:
        return

    pets_snapshot = snapshot_root / "pets"
    if pets_snapshot.exists():
        for package_dir in pets_snapshot.iterdir():
            if package_dir.is_dir():
                destination = PETS_DIR / package_dir.name
                if destination.exists():
                    shutil.rmtree(destination)
                shutil.copytree(package_dir, destination)

    docs_snapshot = snapshot_root / "docs"
    if docs_snapshot.exists():
        for source_file in docs_snapshot.rglob("*"):
            if source_file.is_file():
                destination = ROOT / source_file.relative_to(snapshot_root)
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, destination)


def ensure_output_dirs() -> None:
    for path in [PETS_DIR, SOURCE_DIR, PREVIEW_DIR, SPRITESHEET_DIR, DETAIL_SPRITESHEET_DIR, DOWNLOAD_DIR, DATA_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def detail_atlas_scale_for(package_name: str, profile_package_name: str | None = None) -> int:
    profile = (
        LIVE2D_RENDER_PROFILES.get(package_name)
        or SPINE_RENDER_PROFILES.get(package_name)
        or (LIVE2D_RENDER_PROFILES.get(profile_package_name) if profile_package_name else None)
        or (SPINE_RENDER_PROFILES.get(profile_package_name) if profile_package_name else None)
        or {}
    )
    return int(profile.get("detailAtlasScale", DETAIL_ATLAS_SCALE))


def detail_atlas_scale_from_file(path: Path) -> int:
    if not path.exists():
        return 1
    with Image.open(path) as image:
        expected_width = CELL_W * COLS
        if image.width % expected_width:
            return 1
        return max(1, image.width // expected_width)


def is_local_site_asset(url: str) -> bool:
    return bool(url) and not re.match(r"^(?:[a-z][a-z\d+\-.]*:|#|//)", str(url), flags=re.I)


def site_asset_path(url: str) -> Path:
    clean_url = str(url).split("#", 1)[0].split("?", 1)[0]
    return DOCS_DIR / clean_url


def asset_fingerprint(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()[:16]


def asset_versions_for_entry(entry: dict[str, Any]) -> dict[str, str]:
    versions: dict[str, str] = {}
    for field in ("download", "preview", "spritesheet", "detailSpritesheet", "sourceImage"):
        url = str(entry.get(field) or "")
        if not is_local_site_asset(url):
            continue
        path = site_asset_path(url)
        if path.exists() and path.is_file():
            versions[url] = asset_fingerprint(path)
    return versions


def attach_asset_versions(site_data: dict[str, Any]) -> None:
    for collection_name in ("pets", "cuteVariants"):
        for entry in site_data.get(collection_name, []):
            if isinstance(entry, dict):
                entry["assetVersions"] = asset_versions_for_entry(entry)


def is_hidden_normal_package(package_name: str) -> bool:
    if package_name in HIDDEN_NORMAL_PACKAGES:
        return True
    return any(package_name.startswith(f"9Pets-{slug_suffix(name)}-") for name in HIDDEN_NORMAL_CHARACTERS)


def is_stale_non_default_art_rig_pet(pet: dict[str, Any]) -> bool:
    return (
        not pet.get("isDefaultSkin", True)
        and pet.get("animationMode") == "official-art-elastic-rig"
    )


def normal_skin_skip_reason(
    name: str,
    official_index: dict[str, dict[str, Any]],
    skin_entry: dict[str, Any] | None,
) -> str:
    if skin_entry is None:
        return ""
    skin_name = skin_name_from_entry(skin_entry)
    package_name = package_name_for(name, skin_name)
    if is_hidden_normal_package(package_name):
        return "hidden because this character has no usable Normal Live2D package"

    asset = resolve_official_asset(name, official_index, skin_entry)
    if asset.get("isDefaultSkin") or package_name in NORMAL_SPINE_OVERRIDE_PACKAGES:
        return ""

    cubism_path = asset.get("cubismPath", "")
    if live2d_model_cached(cubism_path):
        return ""
    return f"non-default skin requires cached Live2D source ({cubism_path or 'no mapped Cubism path'})"


def visible_normal_pets(pets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        pet
        for pet in pets
        if not is_hidden_normal_package(pet.get("packageName", ""))
        and not is_stale_non_default_art_rig_pet(pet)
    ]


def catalog_package_lookup(catalog: dict[str, Any], official_index: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    lookup: dict[str, dict[str, Any]] = {}
    for item in catalog["characters"]:
        name = item["name"]
        skins = official_skin_entries(name, official_index)
        if not skins:
            skins = [{"id": "", "characterSkinNameEng": DEFAULT_SKIN_NAME}]
        for skin in skins:
            skin_name = skin_name_from_entry(skin)
            for cute in [False, True]:
                package_name = package_name_for(name, skin_name, cute=cute)
                lookup[package_name] = {
                    "name": name,
                    "skinName": skin_name,
                    "skinEntry": skin,
                    "isDefaultSkin": is_default_skin_name(skin_name),
                    "normalPackageName": package_name_for(name, skin_name),
                    "legacyNormalPackageName": legacy_package_name_for(name),
                    "legacyCutePackageName": legacy_package_name_for(name, cute=True),
                }
        legacy_normal = legacy_package_name_for(name)
        legacy_cute = legacy_package_name_for(name, cute=True)
        default_skin = default_skin_entry(skins) or {"id": "", "characterSkinNameEng": DEFAULT_SKIN_NAME}
        lookup[legacy_normal] = {
            "name": name,
            "skinName": DEFAULT_SKIN_NAME,
            "skinEntry": default_skin,
            "isDefaultSkin": True,
            "normalPackageName": package_name_for(name, DEFAULT_SKIN_NAME),
            "legacyNormalPackageName": legacy_normal,
            "legacyCutePackageName": legacy_cute,
        }
        lookup[legacy_cute] = {
            "name": name,
            "skinName": DEFAULT_SKIN_NAME,
            "skinEntry": default_skin,
            "isDefaultSkin": True,
            "normalPackageName": package_name_for(name, DEFAULT_SKIN_NAME),
            "legacyNormalPackageName": legacy_normal,
            "legacyCutePackageName": legacy_cute,
        }
    return lookup


def make_cute_source_art(package_name: str, atlas_path: Path) -> str:
    output = SOURCE_DIR / f"{package_name}.png"
    if not atlas_path.exists():
        return ""

    with Image.open(atlas_path) as atlas_file:
        atlas = normalize_transparent_pixels(atlas_file.convert("RGBA"))

    atlas_scale = detail_atlas_scale_from_file(atlas_path)
    cell_w = CELL_W * atlas_scale
    cell_h = CELL_H * atlas_scale
    frame = atlas.crop((0, 0, cell_w, cell_h))
    cropped = crop_alpha(frame)
    padding = max(16, 16 * atlas_scale)
    canvas = Image.new("RGBA", (cropped.width + padding * 2, cropped.height + padding * 2), (0, 0, 0, 0))
    canvas.alpha_composite(cropped, (padding, padding))
    save_image_atomic(normalize_transparent_pixels(canvas), output)
    return f"assets/source/{package_name}.png"


def cute_source_info(
    base: dict[str, Any],
    package_name: str,
    source_image: str,
    profile_package_name: str | None = None,
) -> dict[str, Any]:
    info = dict(base)
    override = CUTE_SPINE_SOURCE_OVERRIDES.get(package_name)
    if not override and profile_package_name and info.get("isDefaultSkin", True):
        override = CUTE_SPINE_SOURCE_OVERRIDES.get(profile_package_name)
    if override:
        original_skin_name = info.get("skinName", DEFAULT_SKIN_NAME)
        original_is_default = info.get("isDefaultSkin", True)
        info.update({key: value for key, value in override.items() if key != "skinName"})
        info["skinName"] = original_skin_name
        info["isDefaultSkin"] = original_is_default
        if override.get("spinePath"):
            info["spineUrl"] = repo_tree_url(override["spinePath"])
    spine_path = info.get("spinePath", "")
    spine_url = info.get("spineUrl", "")
    info["sourceImage"] = source_image
    info["sourceUrl"] = spine_url or info.get("assetRepoUrl", "")
    info["sourceRepoPath"] = spine_path or info.get("sourceRepoPath", "")
    info["live2dCacheStatus"] = "cute-rendered"
    info["animationMode"] = "official-cute-spine"
    info["animationModeLabel"] = "Official chibi Spine motion capture"
    return info


def source_info_metadata(
    name: str,
    normal_package: str,
    official_index: dict[str, dict[str, Any]],
    skin_entry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    asset = resolve_official_asset(name, official_index, skin_entry)
    cubism_path = asset.get("cubismPath", "")
    spine_path = asset.get("spinePath", "")
    return {
        "sourceType": OFFICIAL_SOURCE_TYPE,
        "sourceUrl": repo_tree_url(spine_path) or ASSET_REPO_URL,
        "sourceImage": f"assets/source/{normal_package}.png",
        "sourceRepoPath": "",
        "assetId": str(asset["assetId"]),
        "assetRepoUrl": ASSET_REPO_URL,
        "spinePath": spine_path,
        "cubismPath": cubism_path,
        "spineUrl": repo_tree_url(spine_path),
        "cubismUrl": repo_tree_url(cubism_path),
        "birthday": asset.get("birthday", ""),
        "skinName": asset.get("skinName", "Default"),
        "isDefaultSkin": bool(asset.get("isDefaultSkin")),
        "skinDescription": asset.get("skinDescription", ""),
        "matchedName": asset.get("matchedName", name),
        "live2dCacheStatus": "cached" if live2d_model_cached(cubism_path) else ("mapped" if cubism_path else "none"),
        "animationMode": "official-art-elastic-rig",
        "animationModeLabel": "Official art atlas; Live2D path mapped",
    }


def base_source_info_for_cute(
    name: str,
    normal_package: str,
    normal: dict[str, Any] | None,
    official_index: dict[str, dict[str, Any]],
    skin_entry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if normal:
        return dict(normal)
    return source_info_metadata(name, normal_package, official_index, skin_entry)


def build_cute_variants(
    pets: list[dict[str, Any]],
    catalog: dict[str, Any],
    official_index: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    normal_by_package = {pet["packageName"]: pet for pet in pets}
    package_lookup = catalog_package_lookup(catalog, official_index)
    variants: list[dict[str, Any]] = []

    for package_dir in sorted(PETS_DIR.glob(f"{CUTE_PACKAGE_PREFIX}*")):
        if not package_dir.is_dir():
            continue
        package_name = package_dir.name
        package_info = package_lookup.get(package_name)
        if not package_info:
            continue
        name = str(package_info["name"])
        skin_name = str(package_info["skinName"])
        skin_entry = package_info.get("skinEntry")
        normal_package = str(package_info["normalPackageName"])
        normal = normal_by_package.get(normal_package)

        pet_json_path = package_dir / "pet.json"
        if pet_json_path.exists():
            pet_json = json.loads(pet_json_path.read_text(encoding="utf-8"))
        else:
            pet_json = {
                "id": pet_id_from_package(package_name),
                "displayName": f"9Pets Cute - {name} - {skin_name}",
            }

        spritesheet = SPRITESHEET_DIR / f"{package_name}.webp"
        detail_spritesheet = DETAIL_SPRITESHEET_DIR / f"{package_name}.webp"
        preview = PREVIEW_DIR / f"{package_name}.png"
        zip_path = DOWNLOAD_DIR / f"{package_name}.zip"
        if not spritesheet.exists() or not preview.exists() or not zip_path.exists():
            continue

        detail_path = f"assets/detail-spritesheets/{package_name}.webp" if detail_spritesheet.exists() else ""
        source_image = make_cute_source_art(package_name, detail_spritesheet if detail_spritesheet.exists() else spritesheet)
        base_info = base_source_info_for_cute(name, normal_package, normal, official_index, skin_entry if isinstance(skin_entry, dict) else None)
        source_info = cute_source_info(
            base_info,
            package_name,
            source_image or f"assets/previews/{package_name}.png",
            str(package_info["legacyCutePackageName"]),
        )
        variants.append(
            {
                "id": pet_json.get("id", pet_id_from_package(package_name)),
                "packageName": package_name,
                "normalPackageName": normal_package,
                "normalId": normal["id"] if normal else pet_id_from_package(normal_package),
                "displayName": name,
                "skinDisplayName": "" if is_default_skin_name(skin_name) else f"-- {skin_name}",
                "variantType": "cute",
                "variantLabel": "Cute",
                "download": f"downloads/{package_name}.zip",
                "preview": f"assets/previews/{package_name}.png",
                "spritesheet": f"assets/spritesheets/{package_name}.webp",
                "detailSpritesheet": detail_path,
                "detailAtlasScale": detail_atlas_scale_from_file(detail_spritesheet),
                "sourceType": source_info["sourceType"],
                "sourceUrl": source_info["sourceUrl"],
                "sourceImage": source_info["sourceImage"],
                "sourceRepoPath": source_info["sourceRepoPath"],
                "assetId": source_info["assetId"],
                "assetRepoUrl": source_info["assetRepoUrl"],
                "spinePath": source_info["spinePath"],
                "spineUrl": source_info["spineUrl"],
                "cubismPath": source_info["cubismPath"],
                "cubismUrl": source_info["cubismUrl"],
                "birthday": source_info["birthday"],
                "skinName": source_info["skinName"],
                "isDefaultSkin": source_info["isDefaultSkin"],
                "skinDescription": source_info.get("skinDescription", ""),
                "matchedName": source_info["matchedName"],
                "live2dCacheStatus": source_info["live2dCacheStatus"],
                "animationMode": source_info["animationMode"],
                "animationModeLabel": source_info["animationModeLabel"],
                "characterSummary": (
                    f"{name} has a separate cute Codex pet variant, "
                    "preserved from official chibi battle motion frames and packaged apart from the normal Live2D track."
                ),
                "packageBytes": zip_path.stat().st_size,
            }
        )

    return sorted(variants, key=package_sort_key)


def build_pet(
    item: dict[str, Any],
    official_index: dict[str, dict[str, Any]],
    skin_entry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    name = item["name"]
    if skin_entry is None:
        skin_entry = default_skin_entry(official_skin_entries(name, official_index))
    skin_name = skin_name_from_entry(skin_entry or {})
    package_name = package_name_for(name, skin_name)
    profile_package_name = base_profile_package_name(name)
    package_dir = PETS_DIR / package_name
    package_dir.mkdir(parents=True, exist_ok=True)

    sprite, source_info = get_source_sprite(name, package_name, official_index, skin_entry)
    requires_live2d_skin = (
        not source_info["isDefaultSkin"]
        and package_name not in NORMAL_SPINE_OVERRIDE_PACKAGES
    )
    if requires_live2d_skin and not live2d_model_cached(source_info.get("cubismPath", "")):
        raise RuntimeError(
            f"{package_name} requires a cached skin Live2D Cubism source; "
            f"mapped path is {source_info.get('cubismPath') or 'empty'}"
        )

    live2d_frames = None
    if package_name not in NORMAL_SPINE_OVERRIDE_PACKAGES:
        live2d_frames = render_live2d_frames(package_name, source_info.get("cubismPath", ""), profile_package_name)
    spine_frames = None
    detail_atlas: Image.Image | None = None
    detail_atlas_scale = 1
    if live2d_frames:
        try:
            atlas = make_atlas_from_live2d_frames(live2d_frames)
            detail_atlas_scale = detail_atlas_scale_for(package_name, profile_package_name)
            detail_atlas = make_atlas_from_live2d_frames(live2d_frames, cell_scale=detail_atlas_scale)
            source_info["animationMode"] = "official-live2d-cubism"
            source_info["animationModeLabel"] = "Official Live2D Cubism motion capture"
            source_info["live2dCacheStatus"] = "rendered"
        except Exception as error:
            print(f"Live2D atlas compose failed for {package_name}: {error}", flush=True)
            if requires_live2d_skin:
                raise
            atlas = make_atlas(sprite)
            source_info["live2dCacheStatus"] = "compose-failed"
            detail_atlas_scale = 1
    elif spine_frames:
        try:
            atlas = make_atlas_from_live2d_frames(spine_frames)
            detail_atlas_scale = detail_atlas_scale_for(package_name, profile_package_name)
            detail_atlas = make_atlas_from_live2d_frames(spine_frames, cell_scale=detail_atlas_scale)
            source_info["animationMode"] = "official-spine"
            source_info["animationModeLabel"] = "Official Spine motion capture"
            source_info["live2dCacheStatus"] = "spine-rendered"
        except Exception as error:
            print(f"Spine atlas compose failed for {package_name}: {error}", flush=True)
            if requires_live2d_skin:
                raise
            atlas = make_atlas(sprite)
            source_info["live2dCacheStatus"] = "spine-compose-failed"
            detail_atlas_scale = 1
    else:
        if requires_live2d_skin:
            raise RuntimeError(
                f"{package_name} requires rendered skin Live2D frames; "
                f"cache status is {source_info.get('live2dCacheStatus')}"
            )
        atlas = make_atlas(sprite)

    spritesheet_path = package_dir / "spritesheet.webp"
    save_image_atomic(atlas, spritesheet_path, format="WEBP", lossless=True, quality=100, method=0)

    pet_json = make_pet_json(package_name, name, source_info)
    (package_dir / "pet.json").write_text(json.dumps(pet_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    docs_spritesheet = SPRITESHEET_DIR / f"{package_name}.webp"
    shutil.copy2(spritesheet_path, docs_spritesheet)
    detail_spritesheet = ""
    if detail_atlas:
        docs_detail_spritesheet = DETAIL_SPRITESHEET_DIR / f"{package_name}.webp"
        docs_detail_spritesheet.parent.mkdir(parents=True, exist_ok=True)
        save_image_atomic(detail_atlas, docs_detail_spritesheet, format="WEBP", lossless=True, quality=100, method=0)
        detail_spritesheet = f"assets/detail-spritesheets/{package_name}.webp"
    preview_path = PREVIEW_DIR / f"{package_name}.png"
    make_preview_from_atlas(atlas, preview_path)

    zip_path = DOWNLOAD_DIR / f"{package_name}.zip"
    package_bytes = write_zip(package_name, pet_json, spritesheet_path, zip_path, source_info)

    return {
        "id": pet_json["id"],
        "packageName": package_name,
        "displayName": name,
        "skinDisplayName": "" if source_info["isDefaultSkin"] else f"-- {source_info['skinName']}",
        "download": f"downloads/{package_name}.zip",
        "preview": f"assets/previews/{package_name}.png",
        "spritesheet": f"assets/spritesheets/{package_name}.webp",
        "detailSpritesheet": detail_spritesheet,
        "detailAtlasScale": detail_atlas_scale,
        "sourceType": source_info["sourceType"],
        "sourceUrl": source_info["sourceUrl"],
        "sourceImage": source_info["sourceImage"],
        "sourceRepoPath": source_info["sourceRepoPath"],
        "assetId": source_info["assetId"],
        "assetRepoUrl": source_info["assetRepoUrl"],
        "spinePath": source_info["spinePath"],
        "spineUrl": source_info["spineUrl"],
        "cubismPath": source_info["cubismPath"],
        "cubismUrl": source_info["cubismUrl"],
        "birthday": source_info["birthday"],
        "skinName": source_info["skinName"],
        "isDefaultSkin": source_info["isDefaultSkin"],
        "skinDescription": source_info.get("skinDescription", ""),
        "matchedName": source_info["matchedName"],
        "live2dCacheStatus": source_info["live2dCacheStatus"],
        "animationMode": source_info["animationMode"],
        "animationModeLabel": source_info["animationModeLabel"],
        "characterSummary": (
            f"{name} is tracked as an official-sourced Reverse: 1999 character package. "
            f"This build maps asset id {source_info['assetId']} to the game asset dump"
            + (
                " and uses captured Live2D motion frames for the pet atlas."
                if source_info["animationMode"] == "official-live2d-cubism"
                else " and uses captured Spine motion frames for the pet atlas."
                if source_info["animationMode"] == "official-spine"
                else " with mapped Live2D or Spine paths where available."
            )
        ),
        "packageBytes": package_bytes,
    }


def build_cute_pet(
    item: dict[str, Any],
    official_index: dict[str, dict[str, Any]],
    skin_entry: dict[str, Any] | None = None,
) -> str:
    name = item["name"]
    if skin_entry is None:
        skin_entry = default_skin_entry(official_skin_entries(name, official_index))
    skin_name = skin_name_from_entry(skin_entry or {})
    normal_package_name = package_name_for(name, skin_name)
    package_name = package_name_for(name, skin_name, cute=True)
    profile_package_name = base_profile_package_name(name, cute=True)
    package_dir = PETS_DIR / package_name
    package_dir.mkdir(parents=True, exist_ok=True)

    source_info = source_info_metadata(name, normal_package_name, official_index, skin_entry)
    source_info = cute_source_info(source_info, package_name, f"assets/source/{package_name}.png", profile_package_name)

    spine_frames = render_spine_frames(package_name, source_info.get("spinePath", ""), profile_package_name)
    if not spine_frames:
        raise RuntimeError(f"No audited cute Spine render profile is available for {package_name}")

    atlas = make_atlas_from_live2d_frames(spine_frames)
    detail_atlas_scale = detail_atlas_scale_for(package_name, profile_package_name)
    detail_atlas = make_atlas_from_live2d_frames(spine_frames, cell_scale=detail_atlas_scale)

    spritesheet_path = package_dir / "spritesheet.webp"
    save_image_atomic(atlas, spritesheet_path, format="WEBP", lossless=True, quality=100, method=0)

    pet_json = make_pet_json(package_name, name, source_info)
    (package_dir / "pet.json").write_text(json.dumps(pet_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    docs_spritesheet = SPRITESHEET_DIR / f"{package_name}.webp"
    shutil.copy2(spritesheet_path, docs_spritesheet)
    docs_detail_spritesheet = DETAIL_SPRITESHEET_DIR / f"{package_name}.webp"
    docs_detail_spritesheet.parent.mkdir(parents=True, exist_ok=True)
    save_image_atomic(detail_atlas, docs_detail_spritesheet, format="WEBP", lossless=True, quality=100, method=0)
    make_cute_source_art(package_name, docs_detail_spritesheet)
    preview_path = PREVIEW_DIR / f"{package_name}.png"
    make_preview_from_atlas(atlas, preview_path)

    zip_path = DOWNLOAD_DIR / f"{package_name}.zip"
    write_zip(package_name, pet_json, spritesheet_path, zip_path, source_info)
    return package_name


def migrate_default_cute_pet(item: dict[str, Any], official_index: dict[str, dict[str, Any]]) -> str | None:
    name = item["name"]
    skin_entry = default_skin_entry(official_skin_entries(name, official_index))
    if not skin_entry:
        return None

    skin_name = skin_name_from_entry(skin_entry)
    legacy_package = legacy_package_name_for(name, cute=True)
    package_name = package_name_for(name, skin_name, cute=True)
    if legacy_package == package_name:
        return package_name

    package_dir = PETS_DIR / package_name
    legacy_dir = PETS_DIR / legacy_package
    spritesheet_path = package_dir / "spritesheet.webp"
    legacy_spritesheet_path = legacy_dir / "spritesheet.webp"
    if not legacy_spritesheet_path.exists() and not spritesheet_path.exists():
        return None

    package_dir.mkdir(parents=True, exist_ok=True)
    if legacy_spritesheet_path.exists():
        shutil.copy2(legacy_spritesheet_path, spritesheet_path)

    docs_spritesheet = SPRITESHEET_DIR / f"{package_name}.webp"
    legacy_docs_spritesheet = SPRITESHEET_DIR / f"{legacy_package}.webp"
    if legacy_docs_spritesheet.exists():
        shutil.copy2(legacy_docs_spritesheet, docs_spritesheet)
    elif spritesheet_path.exists():
        shutil.copy2(spritesheet_path, docs_spritesheet)

    docs_detail_spritesheet = DETAIL_SPRITESHEET_DIR / f"{package_name}.webp"
    legacy_docs_detail_spritesheet = DETAIL_SPRITESHEET_DIR / f"{legacy_package}.webp"
    if legacy_docs_detail_spritesheet.exists():
        docs_detail_spritesheet.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(legacy_docs_detail_spritesheet, docs_detail_spritesheet)

    _, source_info = get_source_sprite(name, package_name_for(name, skin_name), official_index, skin_entry)
    source_info = cute_source_info(source_info, package_name, f"assets/source/{package_name}.png", legacy_package)
    pet_json = make_pet_json(package_name, name, source_info)
    (package_dir / "pet.json").write_text(json.dumps(pet_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    preview_path = PREVIEW_DIR / f"{package_name}.png"
    with Image.open(spritesheet_path) as atlas_file:
        make_preview_from_atlas(atlas_file.convert("RGBA"), preview_path)

    source_atlas = docs_detail_spritesheet if docs_detail_spritesheet.exists() else docs_spritesheet
    make_cute_source_art(package_name, source_atlas)
    write_zip(package_name, pet_json, spritesheet_path, DOWNLOAD_DIR / f"{package_name}.zip", source_info)

    if legacy_dir.exists():
        shutil.rmtree(legacy_dir)
    for legacy_file in [
        SOURCE_DIR / f"{legacy_package}.png",
        SPRITESHEET_DIR / f"{legacy_package}.webp",
        DETAIL_SPRITESHEET_DIR / f"{legacy_package}.webp",
        PREVIEW_DIR / f"{legacy_package}.png",
        DOWNLOAD_DIR / f"{legacy_package}.zip",
    ]:
        legacy_file.unlink(missing_ok=True)

    return package_name


def migrate_default_cute_pets(catalog: dict[str, Any], official_index: dict[str, dict[str, Any]]) -> list[str]:
    migrated: list[str] = []
    for item in catalog["characters"]:
        package_name = migrate_default_cute_pet(item, official_index)
        if package_name:
            migrated.append(package_name)
    return migrated


def find_catalog_item(catalog: dict[str, Any], selector: str) -> dict[str, Any]:
    selector_key = selector
    if selector_key.startswith(CUTE_PACKAGE_PREFIX):
        selector_key = selector_key.removeprefix(CUTE_PACKAGE_PREFIX)
    else:
        selector_key = selector_key.removeprefix("9Pets-")
    normalized_selector = normalized_lookup_name(selector_key)
    prefix_match: dict[str, Any] | None = None
    for item in catalog["characters"]:
        name = item["name"]
        package_name = package_name_for(name, DEFAULT_SKIN_NAME)
        legacy_package_name = legacy_package_name_for(name)
        candidates = {
            normalized_lookup_name(name),
            normalized_lookup_name(slug_suffix(name)),
            normalized_lookup_name(package_name),
            normalized_lookup_name(legacy_package_name),
            normalized_lookup_name(pet_id_from_package(package_name)),
            normalized_lookup_name(pet_id_from_package(legacy_package_name)),
        }
        base_slug = normalized_lookup_name(slug_suffix(name))
        if normalized_selector in candidates:
            return item
        if prefix_match is None and normalized_selector.startswith(base_slug):
            prefix_match = item
    if prefix_match is not None:
        return prefix_match
    raise RuntimeError(f"No catalog character matches --only {selector}")


def find_skin_entry(
    item: dict[str, Any],
    official_index: dict[str, dict[str, Any]],
    selector: str | None = None,
    explicit_skin: str | None = None,
    *,
    cute: bool = False,
) -> dict[str, Any] | None:
    skins = official_skin_entries(item["name"], official_index)
    if not skins:
        return None
    if explicit_skin:
        normalized_skin = normalized_lookup_name(explicit_skin)
        for skin in skins:
            skin_name = skin_name_from_entry(skin)
            candidates = {
                normalized_lookup_name(skin_name),
                normalized_lookup_name(slug_suffix(skin_name)),
                str(skin.get("id", "")),
            }
            if normalized_skin in candidates:
                return skin
        raise RuntimeError(f"No skin named {explicit_skin!r} for {item['name']}")

    if selector:
        normalized_selector = normalized_lookup_name(selector)
        for skin in skins:
            skin_name = skin_name_from_entry(skin)
            package_name = package_name_for(item["name"], skin_name, cute=cute)
            candidates = {
                normalized_lookup_name(package_name),
                normalized_lookup_name(pet_id_from_package(package_name)),
                normalized_lookup_name(f"{slug_suffix(item['name'])}-{slug_suffix(skin_name)}"),
                str(skin.get("id", "")),
            }
            if normalized_selector in candidates:
                return skin

    return default_skin_entry(skins)


def write_site_data(site_data: dict[str, Any]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    attach_asset_versions(site_data)
    (DATA_DIR / "pets.json").write_text(json.dumps(site_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    data_js = "window.NINEPETS_DATA = " + json.dumps(site_data, ensure_ascii=False) + ";\n"
    data_script = DATA_DIR / "pets-data.js"
    data_script.write_text(data_js, encoding="utf-8")
    update_entrypoint_asset_fingerprints()


def update_entrypoint_asset_fingerprints() -> None:
    assets = {
        "styles.css": DOCS_DIR / "styles.css",
        "app.js": DOCS_DIR / "app.js",
        "pet.js": DOCS_DIR / "pet.js",
        "data/pets-data.js": DATA_DIR / "pets-data.js",
    }
    for entrypoint in (DOCS_DIR / "index.html", DOCS_DIR / "pet.html"):
        if not entrypoint.exists():
            continue
        html = entrypoint.read_text(encoding="utf-8")
        updated = html
        for asset, asset_path in assets.items():
            if not asset_path.exists():
                continue
            fingerprint = hashlib.sha256(asset_path.read_bytes()).hexdigest()[:16]
            escaped = re.escape(asset)
            pattern = re.compile(rf'(?P<attr>href|src)="{escaped}(?:\?v=[0-9a-f]+)?"')
            updated = pattern.sub(rf'\g<attr>="{asset}?v={fingerprint}"', updated)
        if updated != html:
            entrypoint.write_text(updated, encoding="utf-8")


def build(only: str | None = None, cute_only: str | None = None, skin: str | None = None) -> None:
    if only and cute_only:
        raise RuntimeError("Use either --only or --cute-only, not both.")

    catalog = read_catalog()
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    official_index = load_official_asset_index()

    if cute_only:
        ensure_output_dirs()
        site_data_path = DATA_DIR / "pets.json"
        if not site_data_path.exists():
            raise RuntimeError("Single-character cute builds require existing docs/data/pets.json")
        site_data = json.loads(site_data_path.read_text(encoding="utf-8"))
        item = find_catalog_item(catalog, cute_only)
        skin_entry = find_skin_entry(item, official_index, cute_only, skin, cute=True)
        package_name = build_cute_pet(item, official_index, skin_entry)
        pets = visible_normal_pets(site_data.get("pets", []))
        site_data["generatedAt"] = generated_at
        site_data["total"] = len(pets)
        site_data["pets"] = sorted(pets, key=package_sort_key)
        cute_variants = build_cute_variants(pets, catalog, official_index)
        site_data["cuteTotal"] = len(cute_variants)
        site_data["cuteVariants"] = cute_variants
        write_site_data(site_data)
        print(f"Generated one cute pet: {package_name}")
        print(f"Updated site data in {DATA_DIR / 'pets.json'}")
        return

    if only:
        ensure_output_dirs()
        site_data_path = DATA_DIR / "pets.json"
        if not site_data_path.exists():
            raise RuntimeError("Single-character builds require existing docs/data/pets.json")
        site_data = json.loads(site_data_path.read_text(encoding="utf-8"))
        item = find_catalog_item(catalog, only)
        skin_entry = find_skin_entry(item, official_index, only, skin)
        target_package_name = package_name_for(item["name"], skin_name_from_entry(skin_entry or {}))
        skip_reason = normal_skin_skip_reason(item["name"], official_index, skin_entry)
        if skip_reason:
            raise RuntimeError(f"{target_package_name} is {skip_reason}")
        pet_entry = build_pet(item, official_index, skin_entry)
        pets = [
            pet
            for pet in visible_normal_pets(site_data.get("pets", []))
            if pet.get("packageName") != pet_entry["packageName"]
        ]
        if not is_hidden_normal_package(pet_entry["packageName"]):
            pets.append(pet_entry)
        site_data["generatedAt"] = generated_at
        site_data["total"] = len(pets)
        site_data["pets"] = sorted(pets, key=package_sort_key)
        cute_variants = build_cute_variants(pets, catalog, official_index)
        site_data["cuteTotal"] = len(cute_variants)
        site_data["cuteVariants"] = cute_variants
        write_site_data(site_data)
        print(f"Generated one pet: {pet_entry['packageName']}")
        print(f"Updated site data in {DATA_DIR / 'pets.json'}")
        return

    cute_snapshot = snapshot_cute_outputs()
    try:
        clean_output_dirs()
        restore_cute_outputs(cute_snapshot)
    finally:
        if cute_snapshot:
            shutil.rmtree(cute_snapshot, ignore_errors=True)

    official_site_assets = download_official_site_assets()
    pets: list[dict[str, Any]] = []

    for index, item in enumerate(catalog["characters"], start=1):
        skins = official_skin_entries(item["name"], official_index)
        if not skins:
            skins = [{"id": "", "characterSkinNameEng": DEFAULT_SKIN_NAME}]
        for skin_entry in skins:
            skin_name = skin_name_from_entry(skin_entry)
            package_name = package_name_for(item["name"], skin_name)
            skip_reason = normal_skin_skip_reason(item["name"], official_index, skin_entry)
            if skip_reason:
                print(f"[{index}/{len(catalog['characters'])}] skipped normal {package_name}: {skip_reason}", flush=True)
                continue
            pet_entry = build_pet(item, official_index, skin_entry)
            pets.append(pet_entry)
        if index == 1 or index % 10 == 0 or index == len(catalog["characters"]):
            print(f"[{index}/{len(catalog['characters'])}] {item['name']}", flush=True)

    pets = sorted(pets, key=package_sort_key)
    migrated_cute = migrate_default_cute_pets(catalog, official_index)
    if migrated_cute:
        print(f"Migrated {len(migrated_cute)} default cute packages to -Default names", flush=True)

    site_data = {
        "generatedAt": generated_at,
        "total": len(pets),
        "sources": catalog["sources"],
        "notes": catalog["notes"],
        "officialSiteAssets": official_site_assets,
        "pets": pets,
        "cuteTotal": 0,
        "cuteVariants": [],
    }
    cute_variants = build_cute_variants(pets, catalog, official_index)
    site_data["cuteTotal"] = len(cute_variants)
    site_data["cuteVariants"] = cute_variants
    write_site_data(site_data)
    print(f"Generated {len(pets)} pets into {PETS_DIR}")
    print(f"Generated site data into {DATA_DIR / 'pets.json'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build 9Pets packages and GitHub Pages site assets.")
    parser.add_argument("--only", help="Build one character by display name, package name, or pet id.")
    parser.add_argument("--cute-only", help="Build one cute/chibi variant by display name, normal package name, or pet id.")
    parser.add_argument("--skin", help="Build a specific skin by skin display name, skin slug, or asset id.")
    args = parser.parse_args()
    build(only=args.only, cute_only=args.cute_only, skin=args.skin)
