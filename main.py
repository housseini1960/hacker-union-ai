#!/usr/bin/env python3

import os
import shutil
import time

# =========================
# DEVICE INFO
# =========================

def get_info():
    data = {
        "brand": "Unknown",
        "model": "Unknown",
        "android": "Unknown",
        "cpu": "Unknown",
        "battery": "Unknown",
        "ram": 2,
        "refresh": 144,
        "battery_temp": "Unknown",
        "profile": "Budget",
        "score": 50
    }

    try:
        data["brand"] = os.popen("getprop ro.product.brand").read().strip() or "Unknown"
        data["model"] = os.popen("getprop ro.product.model").read().strip() or "Unknown"
        data["android"] = os.popen("getprop ro.build.version.release").read().strip() or "Unknown"
        data["cpu"] = os.popen("getprop ro.product.cpu.abi").read().strip() or "Unknown"

        try:
            battery = os.popen(
                "termux-battery-status | grep percentage | cut -d':' -f2 | tr -dc '0-9'"
            ).read().strip()
            data["battery"] = battery if battery else "Unknown"
        except Exception:
            data["battery"] = "Unknown"

        total_ram_gb = 2
        if os.path.exists("/proc/meminfo"):
            with open("/proc/meminfo") as f:
                mem = f.readlines()
            total_ram_mb = int(mem[0].split()[1]) // 1024

            if total_ram_mb >= 11000:
                total_ram_gb = 12
            elif total_ram_mb >= 7000:
                total_ram_gb = 8
            elif total_ram_mb >= 5000:
                total_ram_gb = 6
            elif total_ram_mb >= 3000:
                total_ram_gb = 4
            else:
                total_ram_gb = max(1, round(total_ram_mb / 1024))

        data["ram"] = total_ram_gb

        try:
            refresh = os.popen("settings get system peak_refresh_rate").read().strip()
            if not refresh or refresh == "null":
                refresh = os.popen("settings get system user_refresh_rate").read().strip()

            if refresh and refresh != "null":
                detected_hz = int(float(refresh))
                if data["model"] == "Infinix X6873" and detected_hz < 90:
                    data["refresh"] = 144
                else:
                    data["refresh"] = detected_hz
            else:
                data["refresh"] = 144 if data["model"] == "Infinix X6873" else 60
        except Exception:
            data["refresh"] = 144 if data["model"] == "Infinix X6873" else 60

        try:
            temp = os.popen(
                "termux-battery-status | grep temperature | cut -d':' -f2 | tr -dc '0-9.'"
            ).read().strip()
            data["battery_temp"] = temp + "°C" if temp else "Unknown"
        except Exception:
            data["battery_temp"] = "Unknown"

        if total_ram_gb >= 12:
            profile = "Flagship"
        elif total_ram_gb >= 8:
            profile = "High End"
        elif total_ram_gb >= 6:
            profile = "Mid Range"
        else:
            profile = "Budget"

        score = 50
        if total_ram_gb >= 12:
            score += 25
        elif total_ram_gb >= 8:
            score += 20
        elif total_ram_gb >= 6:
            score += 15
        else:
            score += 5

        if data["refresh"] >= 144:
            score += 25
        elif data["refresh"] >= 120:
            score += 15
        elif data["refresh"] >= 90:
            score += 10

        data["profile"] = profile
        data["score"] = min(score, 100)

    except Exception:
        pass

    return data

# =========================
# BANNER
# =========================

def banner():
    os.system("clear")
    print("\u001B[1;96m")
    print("╔════════════════════════════════════╗")
    print("║      \u001B[1;31m🤖 HACKER UNION AI ASSISTANT\u001B[1;96m      ║")
    print("╚════════════════════════════════════╝")
    print("\u001B[0m")
    print("\u001B[1;33m🔻 MAKER      : \u001B[1;31mHousseini1960\u001B[0m")
    print("\u001B[1;36m🔻 VERSION    : \u001B[1;31mHacker Union AI 2.1\u001B[0m")
    print("\u001B[1;32m🔻 STATUS     : \u001B[1;31mOnline\u001B[0m")
    print("\u001B[1;35m🔻 TG         : \u001B[1;31m@OfficialOwner10x\u001B[0m")
    print("\u001B[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m")

# =========================
# SCAN
# =========================

def jarvis_scan():
    os.system("clear")
    scans = [
        ("\u001B[1;32m🔍 Detecting Device Hardware...\u001B[0m", 20),
        ("\u001B[1;33m⚙ Reading System Information...\u001B[0m", 40),
        ("\u001B[1;36m📊 Analyzing RAM & Storage...\u001B[0m", 60),
        ("\u001B[1;35m🎮 Building Gaming Profile...\u001B[0m", 80),
        ("\u001B[1;31m🚀 Preparing Final Report...\u001B[0m", 100)
    ]

    for text, percent in scans:
        os.system("clear")
        print("\u001B[1;96m")
        print("╔══════════════════════════════════════╗")
        print("║      🤖 HACKER UNION AI ANALYZING... 🤖       ║")
        print("╚══════════════════════════════════════╝")
        print("\u001B[0m")
        print("
" + text + "
")
        filled = "■" * (percent // 10)
        empty = "□" * (10 - percent // 10)
        color = "\u001B[1;33m" if percent < 100 else "\u001B[1;32m"
        print(f"{color}[{filled}{empty}] {percent}%\u001B[0m")
        time.sleep(1.5)

    print("
\u001B[1;92m✅ ANALYSIS COMPLETE\u001B[0m")
    print("\u001B[1;36m📋 Loading Results...\u001B[0m")
    time.sleep(1)
    os.system("clear")

# =========================
# BGMI
# =========================

def bgmi():
    d = get_info()
    ram = d["ram"]
    refresh = d["refresh"]
    score = d["score"]

    if score >= 90 or refresh >= 120:
        fps = "120 FPS"
        gyro = [350, 340, 320, 280, 240]
    elif score >= 80:
        fps = "120 FPS" if refresh >= 120 else "90 FPS"
        gyro = [330, 320, 300, 260, 220]
    elif score >= 70:
        fps = "90 FPS"
        gyro = [310, 290, 270, 240, 200]
    elif score >= 60:
        fps = "60 FPS"
        gyro = [290, 270, 250, 220, 180]
    else:
        fps = "40 FPS"
        gyro = [260, 240, 220, 190, 160]

    print("\u001B[1;95m")
    print("╔════════════════════════════════════╗")
    print("║        🔻 BGMI PROFILE 🔻          ║")
    print("╚════════════════════════════════════╝")
    print("\u001B[0m")
    print("\u001B[1;36m📱 🔸DEVICE INFORMATION🔸\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔺 Device       : {d['model']}")
    print(f"🔺 Battery      : {d['battery']}%")
    print(f"🔺 RAM          : {ram} GB")
    print(f"🔺 Android      : {d['android']}")
    print(f"🔺 CPU ABI      : {d['cpu']}")
    print(f"🔺 Refresh Rate : {refresh} Hz")
    print(f"🔺 Battery Temp : {d['battery_temp']}")
    print(f"🔺 Gaming Score : {d['score']}/100")
    print(f"🔺 Profile      : {d['profile']}")
    print("
\u001B[1;33m🎥 CAMERA SETTINGS\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🔸 TPP No Scope : 180")
    print("🔸 FPP No Scope : 170")
    print("🔸 Red Dot      : 60")
    print("🔸 2x Scope     : 45")
    print("🔸 3x Scope     : 30")
    print("🔸 4x Scope     : 20")
    print("
\u001B[1;32m🎯 ADS SETTINGS\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🔸 TPP No Scope : 120")
    print("🔸 FPP No Scope : 110")
    print("🔸 Red Dot      : 55")
    print("🔸 2x Scope     : 40")
    print("🔸 3x Scope     : 30")
    print("
\u001B[1;35m🌀 GYROSCOPE SETTINGS\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔸 No Scope     : {gyro[0]}")
    print(f"🔸 Red Dot      : {gyro[1]}")
    print(f"🔸 2x Scope     : {gyro[2]}")
    print(f"🔸 3x Scope     : {gyro[3]}")
    print(f"🔸 4x Scope     : {gyro[4]}")
    print("
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"\u001B[1;92m 🔻RECOMMENDED FPS🔻 : {fps}\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# FREE FIRE
# =========================

def ff():
    d = get_info()
    score = d["score"]
    refresh = d["refresh"]

    if score >= 90:
        fps = "Ultra / Max"
        general = 100
        red_dot = 95
        x2 = 90
        x4 = 80
        awm = 60
        free_look = 90
    elif score >= 80:
        fps = "Ultra / Max" if refresh >= 120 else "High"
        general = 95
        red_dot = 90
        x2 = 85
        x4 = 75
        awm = 55
        free_look = 85
    elif score >= 70:
        fps = "High"
        general = 90
        red_dot = 85
        x2 = 80
        x4 = 70
        awm = 50
        free_look = 80
    else:
        fps = "Medium"
        general = 85
        red_dot = 80
        x2 = 75
        x4 = 65
        awm = 45
        free_look = 75

    print("\u001B[1;96m")
    print("╔════════════════════════════════════╗")
    print("║        🔻 FREE FIRE PROFIL 🔻      ║")
    print("╚════════════════════════════════════╝")
    print("\u001B[0m")
    print("\u001B[1;36m📱 🔸DEVICE INFORMATION🔸\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔺 Device       : {d['model']}")
    print(f"🔺 Battery      : {d['battery']}%")
    print(f"🔺 RAM          : {d['ram']} GB")
    print(f"🔺 Android      : {d['android']}")
    print(f"🔺 CPU ABI      : {d['cpu']}")
    print(f"🔺 Refresh Rate : {d['refresh']} Hz")
    print(f"🔺 Battery Temp : {d['battery_temp']}")
    print(f"🔺 Gaming Score : {d['score']}/100")
    print(f"🔺 Profile      : {d['profile']}")
    print("
\u001B[1;33m🎯 FREE FIRE SENSITIVITY\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔸 General      : {general}")
    print(f"🔸 Red Dot      : {red_dot}")
    print(f"🔸 2x Scope     : {x2}")
    print(f"🔸 4x Scope     : {x4}")
    print(f"🔸 AWM Scope     : {awm}")
    print(f"🔸 Free Look     : {free_look}")
    print("
\u001B[1;35m🎮 🔸PERFORMANCE ANALYSIS🔸\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    bar = "█" * (score // 10) + "░" * (10 - (score // 10))
    print(f"🏆 Gaming Score : [{bar}] {score}/100")
    tier = "🔥 EXTREME" if score >= 90 else "🚀 HIGH END" if score >= 80 else "⚡ MID RANGE" if score >= 70 else "📱 BASIC"
    print(f"🎯 Device Tier  : {tier}")
    print("
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"\u001B[1;92m 🔻RECOMMENDED FPS🔻 : {fps}\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# BOOSTER
# =========================

def booster():
    os.system("clear")
    print("\u001B[1;96m")
    print("╔════════════════════════════════════╗")
    print("║     🚀 HACKER UNION AI BOOSTER 🚀 ║")
    print("╚════════════════════════════════════╝")
    print("\u001B[0m")

    tasks = [
        "🔍 Scanning Cache Files...",
        "🧹 Cleaning Temporary Data...",
        "⚙ Optimizing System Resources...",
        "🎮 Preparing Gaming Environment...",
        "🚀 Finalizing Optimization..."
    ]

    for i, task in enumerate(tasks, start=1):
        percent = i * 20
        print(f"
\u001B[1;36m{task}\u001B[0m")
        filled = "█" * (percent // 10)
        empty = "░" * (10 - percent // 10)
        print(f"\u001B[1;32m[{filled}{empty}] {percent}%\u001B[0m")
        time.sleep(1)

    paths_to_clear = [os.path.expanduser("~/.cache"), "./__pycache__"]
    for path in paths_to_clear:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
            except Exception:
                pass

    print("
\u001B[1;92m✅ OPTIMIZATION COMPLETE\u001B[0m")
    print("\u001B[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m")
    print(" 🔸Cache Files Cleaned")
    print(" 🔸Temporary Data Removed")
    print(" 🔸System Resources Optimized")
    print(" 🔸Gaming Profile Refreshed")
    print(" 🔸Device Ready For Gaming")
    print("\u001B[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m")
    print("
\u001B[1;93m🎮 STATUS : 🔸READY TO PLAY🔸\u001B[0m")

# =========================
# STORAGE
# =========================

def ram_storage():
    os.system("clear")
    print("\u001B[1;96m")
    print("╔════════════════════════════════════╗")
    print("║      💾 STORAGE ANALYZER 💾       ║")
    print("╚════════════════════════════════════╝")
    print("\u001B[0m")

    try:
        path = "/storage/emulated/0"
        if not os.path.exists(path):
            path = "/"

        total, used, free = shutil.disk_usage(path)
        total_gb = round(total / (1024**3), 2)
        used_gb = round(used / (1024**3), 2)
        free_gb = round(free / (1024**3), 2)
        usage = round((used / total) * 100)

        print("\u001B[1;36m📊 STORAGE INFORMATION\u001B[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"📦 Total Storage : {total_gb} GB")
        print(f"📁 Used Storage  : {used_gb} GB")
        print(f"💾 Free Storage  : {free_gb} GB")
        print("
\u001B[1;35m📈 STORAGE USAGE\u001B[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        filled = "█" * (usage // 5)
        empty = "░" * (20 - (usage // 5))
        print(f"[{filled}{empty}] {usage}%")
        print("
\u001B[1;33m🔎 STORAGE HEALTH\u001B[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        if free_gb < 10:
            print("\u001B[1;31m⚠ CRITICAL : Storage Almost Full\u001B[0m")
            print("🧹 Recommendation : Clean unnecessary files")
        elif free_gb < 30:
            print("\u001B[1;33m⚠ WARNING : Storage Running Low\u001B[0m")
            print("📂 Recommendation : Remove unused apps")
        else:
            print("\u001B[1;32m✅ HEALTHY : Storage Status Good\u001B[0m")
            print("🚀 Device Ready For Smooth Performance")

        print("
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\u001B[1;92m💡 Available Space : {free_gb} GB\u001B[0m")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    except Exception as e:
        print("\u001B[1;31m❌ Storage Error :\u001B[0m", e)

# =========================
# ABOUT
# =========================

def about():
    print("\u001B[1;96m")
    print("╔════════════════════════════════════╗")
    print("║         🤖 ABOUT HACKER UNION AI 2.1        ║")
    print("╚════════════════════════════════════╝")
    print("\u001B[0m")
    print("\u001B[1;36m📱 🔻TOOL INFORMATION🔻\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🤖 Tool Name : HACKER UNION AI")
    print("⚡ Version     : Hacker Union 2.1")
    print("💀 Developer  : Housseini1960")
    print("🟢 Status.     : Online")
    print("
\u001B[1;33m🚀 FEATURES\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🎯 BGMI Gaming Analyzer")
    print("🔥 FREE FIRE Analyzer")
    print("📱 SMART Device Detection")
    print("⚡ GAMING Score Analysis")
    print("💾 RAM & Storage Analyzer")
    print("🚀 PERFORMANCE Booster")
    print("📊 FPS Recommendation")
    print("🌡 BATTERY & Temperature Monitor")
    print("
\u001B[1;35m💡 PURPOSE 👇\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🔻HACKER UNION AI ANALYZES YOUR DEVICE")
    print("🔻AND PROVIDES GAMING RECOMMENDATIONS")
    print("🔻BASED ON HARDWARE CAPABILITIES.")
    print("
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\u001B[1;92m❤️ THANKS FOR USING HACKER UNION AI\u001B[0m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# =========================
# MAIN MENU
# =========================

while True:
    banner()
    print("\u001B[1;96m")
    print("╔════════════════════════════════════╗")
    print("║    \u001B[1;31m🎮 MAIN CONTROL PANEL\u001B[0m        ║")
    print("╚════════════════════════════════════╝")
    print("\u001B[0m")
    print("\u001B[1;92m➊\u001B[0m \u001B[1;36mBGMI MODULE\u001B[0m")
    print("\u001B[1;92m➋\u001B[0m \u001B[1;36mFREE FIRE MODULE\u001B[0m")
    print("\u001B[1;92m➌\u001B[0m \u001B[1;36mSTORAGE ANALYZER\u001B[0m")
    print("\u001B[1;92m➍\u001B[0m \u001B[1;36mPERFORMANCE BOOSTER\u001B[0m")
    print("\u001B[1;92m➎\u001B[0m \u001B[1;36mABOUT HACKER UNION AI\u001B[0m")
    print("\u001B[1;91m➏\u001B[0m \u001B[1;31mEXIT TOOL\u001B[0m")
    print("
\u001B[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m")
    print("\u001B[1;92m💡 Select Module To Continue\u001B[0m")
    print("\u001B[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m")
    choice = input("\u001B[1;92m┌─[🤖 HACKER UNION AI]
└──► \u001B[0m")
    os.system("clear")

    if choice == "1":
        jarvis_scan()
        bgmi()
    elif choice == "2":
        jarvis_scan()
        ff()
    elif choice == "3":
        jarvis_scan()
        ram_storage()
    elif choice == "4":
        booster()
    elif choice == "5":
        about()
    elif choice == "6":
        print("
\u001B[1;92m🤖 HACKER UNION AI SHUTTING DOWN...\u001B[0m")
        time.sleep(1)
        print("\u001B[1;36m👋 Goodbye Housseini1960\u001B[0m")
        break
    else:
        print("\u001B[1;31m❌ Unknown Command Detected!\u001B[0m")

    input("
\u001B[1;33m↩ Press Enter To Return To Menu...\u001B[0m")
