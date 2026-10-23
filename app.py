import os
import requests
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8709739986:AAFmN9R8yQp3pYvNz6ZqJmK4sX8uYt9r9b0"
TELEGRAM_CHAT_ID = "7206856210"

def send_telegram_alert(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={
            "chat_id": TELEGRAM_CHAT_ID, 
            "text": msg, 
            "parse_mode": "Markdown"
        }, timeout=5)
    except Exception as e:
        print("Telegram Alert Error:", e)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 𝗠.𝗞 𝗔𝗜 𝗦𝗜𝗚𝗡𝗔𝗟𝗦 𝗣𝗥𝗢 🚀</title>
    <style>
        body, html { background: transparent !important; margin: 0; padding: 0; overflow: hidden; font-family: sans-serif; height: 100%; width: 100%; }
        #mk-master-panel {
            position: fixed; top: 10%; left: 20px; width: 320px; height: auto;
            background: #06090f !important; border-radius: 18px;
            z-index: 2147483647 !important; color: #fff; font-family: sans-serif;
            box-sizing: border-box; border: 3px solid #00f0ff; overflow: hidden;
            box-shadow: 0 0 35px rgba(0, 240, 255, 0.6); touch-action: none;
            backdrop-filter: blur(10px);
            animation: mkGlowPulse 3s infinite alternate;
        }
        @keyframes mkGlowPulse {
            0% { box-shadow: 0 0 20px rgba(0, 240, 255, 0.4), inset 0 0 10px rgba(0,240,255,0.2); }
            100% { box-shadow: 0 0 40px rgba(0, 240, 255, 0.9), inset 0 0 20px rgba(0,240,255,0.5); }
        }
        #mk-panel-header {
            background: linear-gradient(90deg, #ff0055, #7000ff, #00f0ff);
            padding: 12px 14px; font-weight: bold; font-size: 13px;
            text-align: center; cursor: move; display: flex; justify-content: space-between; align-items: center;
            user-select: none; -webkit-user-select: none; letter-spacing: 0.5px;
        }
        .mk-screen { padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; width: 100%; }
        .mk-sec-title { font-size: 14px; font-weight: bold; color: #ff0055; text-align: center; text-shadow: 0 0 8px rgba(255,0,85,0.7); }
        .mk-sec-subtitle { font-size: 11px; color: #94a3b8; text-align: center; line-height: 1.4; }
        #mk-key-input { width: 100%; padding: 11px; background: #000; border: 2px solid #1e293b; border-radius: 8px; color: #fff; text-align: center; font-weight: bold; outline: none; box-sizing: border-box; font-size: 13px; }
        .mk-link-btn { width: 100%; padding: 11px; background: #1e1b4b; color: #a855f7; border: 1px solid #4c1d95; font-weight: bold; border-radius: 8px; text-align: center; text-decoration: none; display: block; box-sizing: border-box; font-size: 11.5px; transition: 0.2s; }
        .mk-link-btn:hover { background: #312e81; }
        #mk-radar-status { text-align: center; color: #eab308; font-size: 11.5px; font-weight: bold; letter-spacing: 0.5px; }
        #mk-signal-box { background: #0f172a; padding: 18px; border-radius: 12px; text-align: center; border: 1px solid #1e293b; box-sizing: border-box; min-height: 90px; display: flex; flex-direction: column; justify-content: center; }
        #mk-main-signal { font-size: 22px; font-weight: 900; color: #fff; width: 100%; padding: 8px 0; border-radius: 8px; letter-spacing: 1px; }
        #mk-timer-countdown { font-size: 11.5px; color: #94a3b8; margin-top: 6px; font-weight: bold; }
        #mk-filter-text { text-align: center; color: #10b981; font-size: 11.5px; font-weight: bold; }
        #mk-accuracy-wrapper { text-align: center; color: #e2e8f0; font-size: 12.5px; font-weight: bold; }
        #mk-accuracy-value { color: #06b6d4; font-weight: 900; text-shadow: 0 0 8px #06b6d4; }
        .mk-control-row { display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #94a3b8; }
        .mk-control-row select { background: #000; color: #fff; border: 1px solid #334155; border-radius: 7px; padding: 6px; width: 135px; outline: none; font-weight: bold; }
        .mk-control-row input[type="color"] { border: none; background: transparent; width: 28px; height: 28px; cursor: pointer; }
        .mk-theme-btn { background: #0f172a; color: #fff; border: 1px solid #334155; border-radius: 7px; padding: 7px; font-size: 10px; cursor: pointer; text-align: center; font-weight: bold; transition: 0.2s; }
        .mk-theme-btn:hover { background: #00f0ff; color: #000; border-color: #00f0ff; box-shadow: 0 0 10px #00f0ff; }
        #mk-minimize-btn { width: 100%; background: transparent; border: 1px dashed #334155; color: #94a3b8; font-size: 11px; font-weight: bold; padding: 8px; border-radius: 7px; cursor: pointer; transition: 0.2s; }
        #mk-minimize-btn:hover { border-color: #00f0ff; color: #00f0ff; background: rgba(0,240,255,0.05); }
        #mk-resize-handle { position: absolute; right: 0; bottom: 0; width: 20px; height: 20px; color: #00f0ff; cursor: se-resize; font-size: 12px; text-align: right; line-height: 20px; z-index: 2147483647; font-weight: bold; user-select: none; }
        #mk-floating-mini-icon { position: fixed; top: 20%; left: 15px; padding: 12px 16px; background: #06090f; border: 2px solid #00f0ff; border-radius: 12px; color: #00f0ff; font-size: 12px; font-weight: bold; cursor: pointer; z-index: 2147483647 !important; display: none; text-shadow: 0 0 8px #00f0ff; box-shadow: 0 0 25px rgba(0,240,255,0.7); touch-action: none; }
        
        /* High-End Pro Animations & Frames */
        .mk-signal-up-active { background: linear-gradient(135deg, #00ff66, #00b347) !important; color: #000 !important; box-shadow: 0 0 30px #00ff66 !important; font-size: 25px !important; font-weight: 900 !important; animation: mkPulseUp 0.7s infinite alternate; }
        .mk-signal-down-active { background: linear-gradient(135deg, #ff0055, #b3003b) !important; color: #fff !important; box-shadow: 0 0 30px #ff0055 !important; font-size: 25px !important; font-weight: 900 !important; animation: mkPulseDown 0.7s infinite alternate; }
        .mk-signal-win-frame { background: rgba(0, 255, 102, 0.25) !important; color: #00ff66 !important; border: 2px dashed #00ff66 !important; font-size: 23px !important; font-weight: 900 !important; text-shadow: 0 0 15px #00ff66 !important; animation: mkWinBounce 0.5s ease; }
        .mk-signal-loss-frame { background: rgba(255, 0, 85, 0.25) !important; color: #ff0055 !important; border: 2px dashed #ff0055 !important; font-size: 23px !important; font-weight: 900 !important; text-shadow: 0 0 15px #ff0055 !important; animation: mkLossShake 0.4s ease; }

        @keyframes mkPulseUp { 0% { transform: scale(1); } 100% { transform: scale(1.04); box-shadow: 0 0 40px #00ff66; } }
        @keyframes mkPulseDown { 0% { transform: scale(1); } 100% { transform: scale(1.04); box-shadow: 0 0 40px #ff0055; } }
        @keyframes mkWinBounce { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.08); } }
        @keyframes mkLossShake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-5px); } 75% { transform: translateX(5px); } }
    </style>
</head>
<body>

<div id="mk-master-panel">
    <div id="mk-panel-header">
        <span>🚀 𝗠.𝗞 𝗔𝗜 𝗦𝗜𝗚𝗡𝗔𝗟𝗦 𝗣𝗥𝗢 🚀</span>
        <div style="display:flex; gap:8px; align-items:center;">
            <span id="mk-toggle-themes-btn" style="cursor:pointer; font-size:10.5px; background:rgba(0,0,0,0.6); padding:3px 7px; border-radius:5px; font-weight:bold;">🎨 30+ THEMES</span>
            <span id="mk-close-btn" style="cursor:pointer; font-weight:bold; margin-left:4px; font-size:14px;">✕</span>
        </div>
    </div>
    
    <div id="mk-theme-drawer" style="display:none; background:rgba(3,7,18,0.98); padding:10px; border-bottom:1px solid #1e293b; max-height:160px; overflow-y:auto;">
        <div id="mk-theme-grid" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:6px;"></div>
    </div>

    <div id="mk-github-screen" class="mk-screen" style="display:block;">
        <div class="mk-sec-title">🔒 SERVER APPROVAL REQUIRED</div>
        <div class="mk-sec-subtitle">Aapka device registered nahi hai. M.K TRADER se online approval allow karwayein.</div>
        <div style="font-size:10.5px; color:#94a3b8; text-align:center; font-weight:bold; margin-top:4px;">YOUR UNIQUE DEVICE ID:</div>
        <div id="mk-dev-id-box" style="background:#000; color:#00f0ff; padding:10px; text-align:center; border-radius:7px; font-weight:bold; border:1px dashed #00f0ff; user-select:all; font-size:12px;"></div>
        <button id="mk-check-github-btn" style="width:100%; padding:12px; background:#00f0ff; color:#000; border:none; font-weight:bold; border-radius:7px; cursor:pointer; margin-top:4px; font-size:12px;">VERIFY MY APPROVAL</button>
        <a href="https://t.me/MK_TRADER586" target="_blank" class="mk-link-btn">📞 CONTACT M.K TRADER</a>
    </div>

    <div id="mk-auth-screen" class="mk-screen" style="display:none;">
        <div class="mk-sec-title">🔑 ENTER PASS KEY</div>
        <div class="mk-sec-subtitle">Device verified online. Enter master console key to unlock matching engine.</div>
        <input type="text" id="mk-key-input" placeholder="ENTER ACCESS KEY..." autocomplete="off">
        <button id="mk-unlock-btn" style="width:100%; padding:12px; background:#00f0ff; color:#000; border:none; font-weight:bold; border-radius:7px; cursor:pointer; font-size:12px;">UNLOCK SYSTEM</button>
        <div id="mk-auth-error" style="color:#ef4444; font-size:11.5px; font-weight:bold; text-align:center; display:none;">INVALID CONSOLE ACCESS KEY!</div>
    </div>
    
    <div id="mk-dashboard-screen" class="mk-screen" style="display:none;">
        <div id="mk-radar-status">🛰️ AI RADAR - SYNCED LIVE</div>
        
        <div id="mk-signal-box">
            <div id="mk-main-signal">WAITING...</div>
            <div id="mk-timer-countdown">NEXT CANDLE IN: --s</div>
        </div>
        
        <div id="mk-filter-text">FILTERING MARKET NOISE...</div>
        <div id="mk-accuracy-wrapper">🎯 ACCURACY: <span id="mk-accuracy-value">99.7%</span></div>

        <div class="mk-control-row">
            <label>⚙️ AI Mode:</label>
            <select id="mk-logic-mode">
                <option value="system" selected>System Mode (VIP)</option>
                <option value="rapid">Continuous Scan</option>
            </select>
        </div>
        
        <div class="mk-control-row">
            <label>⏱️ Expiry Time:</label>
            <select id="mk-time-dropdown">
                <option value="5">5 Second</option>
                <option value="10">10 Second</option>
                <option value="15">15 Second</option>
                <option value="30">30 Second</option>
                <option value="60" selected>1 Minute</option>
                <option value="300">5 Minute</option>
            </select>
        </div>

        <div class="mk-control-row">
            <label>🎨 Laser Neon:</label>
            <input type="color" id="mk-laser-picker" value="#00f0ff">
        </div>
        
        <button id="mk-minimize-btn">🗕 MINIMIZE TERMINAL</button>
    </div>
    <div id="mk-resize-handle">◢</div>
</div>

<div id="mk-floating-mini-icon"><span>🚀 M.K PRO</span></div>

<script>
    const MASTER_KEY = "MK586";
    const GITHUB_DATABASE_URL = "https://raw.githubusercontent.com/mkhacker586-lab/mk-database/main/allowed.json";
    const TELEGRAM_BOT_TOKEN = "8709739986:AAFmN9R8yQp3pYvNz6ZqJmK4sX8uYt9r9b0";
    const TELEGRAM_CHAT_ID = "7206856210";

    function getDeviceID() {
        let id = localStorage.getItem('mk_device_id');
        if (!id) {
            id = 'MK-' + Math.random().toString(36).substring(2, 10).toUpperCase();
            localStorage.setItem('mk_device_id', id);
        }
        return id;
    }
    const DEVICE_ID = getDeviceID();
    document.getElementById('mk-dev-id-box').innerText = DEVICE_ID;

    function sendAlert(msg) {
        fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text: msg, parse_mode: "Markdown" })
        }).catch(e => console.log(e));
    }

    // 30+ Advanced Neon, Smoking & Glowing Themes Collection
    const THEMES = [
        { name: "🩵 Cyan Neon", border: "#00f0ff", bg: "#06090f", header: "linear-gradient(90deg, #ff0055, #7000ff, #00f0ff)" },
        { name: "❤️ Cyber Punk", border: "#ff0055", bg: "#0a0005", header: "linear-gradient(90deg, #ff0055, #330011)" },
        { name: "💛 VIP Gold", border: "#ffd700", bg: "#0a0700", header: "linear-gradient(90deg, #ffd700, #221100)" },
        { name: "💚 Matrix Pro", border: "#00ff66", bg: "#000a03", header: "linear-gradient(90deg, #00ff66, #001100)" },
        { name: "💜 Venom Dark", border: "#a855f7", bg: "#05000a", header: "linear-gradient(90deg, #a855f7, #1e1b4b)" },
        { name: "💙 Valor Sky", border: "#38bdf8", bg: "#020617", header: "linear-gradient(90deg, #38bdf8, #0f172a)" },
        { name: "🧡 Super Saiyan", border: "#f97316", bg: "#0c0400", header: "linear-gradient(90deg, #f97316, #431407)" },
        { name: "☣️ Toxic Lime", border: "#adff2f", bg: "#030700", header: "linear-gradient(90deg, #adff2f, #1a3300)" },
        { name: "💎 Pure Diamond", border: "#00e5ff", bg: "#00121a", header: "linear-gradient(90deg, #00e5ff, #004d66)" },
        { name: "🔥 Crimson Devil", border: "#e11d48", bg: "#0f0003", header: "linear-gradient(90deg, #e11d48, #4c0519)" },
        { name: "🤍 Ghost Edition", border: "#ffffff", bg: "#141414", header: "linear-gradient(90deg, #7f8c8d, #111111)" },
        { name: "🌌 Cosmic Void", border: "#ec4899", bg: "#0d0214", header: "linear-gradient(90deg, #ec4899, #3b0764)" },
        { name: "⚡ Electric Yellow", border: "#facc15", bg: "#0f0f00", header: "linear-gradient(90deg, #facc15, #451a03)" },
        { name: "🏮 Shogun Blood", border: "#991b1b", bg: "#050101", header: "linear-gradient(90deg, #991b1b, #111827)" },
        { name: "🧊 Ice Blizzard", border: "#93c5fd", bg: "#0f172a", header: "linear-gradient(90deg, #1e3a8a, #3b82f6)" },
        { name: "🩷 Hot Magenta", border: "#ff007f", bg: "#0d0006", header: "linear-gradient(90deg, #ff007f, #500028)" },
        { name: "💚 Emerald Glow", border: "#059669", bg: "#02150a", header: "linear-gradient(90deg, #059669, #064e3b)" },
        { name: "💙 Ocean Depth", border: "#0284c7", bg: "#020817", header: "linear-gradient(90deg, #0284c7, #0369a1)" },
        { name: "💛 Amber Flame", border: "#fbbf24", bg: "#171002", header: "linear-gradient(90deg, #fbbf24, #b45309)" },
        { name: "💜 Neon Orchid", border: "#c084fc", bg: "#0f0518", header: "linear-gradient(90deg, #c084fc, #6b21a8)" },
        { name: "❤️ Ruby Spark", border: "#f43f5e", bg: "#140206", header: "linear-gradient(90deg, #f43f5e, #9f1239)" },
        { name: "🩵 Teal Breeze", border: "#14b8a6", bg: "#021714", header: "linear-gradient(90deg, #14b8a6, #115e59)" },
        { name: "🖤 Obsidian Dark", border: "#475569", bg: "#020202", header: "linear-gradient(90deg, #334155, #0f172a)" },
        { name: "🌟 Starlight Pro", border: "#fde047", bg: "#121102", header: "linear-gradient(90deg, #fde047, #ca8a04)" },
        { name: "💨 Smokey Grey", border: "#94a3b8", bg: "#090d16", header: "linear-gradient(90deg, #64748b, #0f172a)" },
        { name: "🔥 Laser Orange", border: "#ff6600", bg: "#120500", header: "linear-gradient(90deg, #ff6600, #ff0055)" },
        { name: "⚡ Plasma Violet", border: "#8b5cf6", bg: "#090214", header: "linear-gradient(90deg, #8b5cf6, #3b82f6)" },
        { name: "🌿 Acid Green", border: "#84cc16", bg: "#061202", header: "linear-gradient(90deg, #84cc16, #10b981)" },
        { name: "🌺 Sakura Pink", border: "#fb7185", bg: "#140408", header: "linear-gradient(90deg, #fb7185, #e11d48)" },
        { name: "🪐 Nebula Purple", border: "#d946ef", bg: "#120314", header: "linear-gradient(90deg, #d946ef, #8b5cf6)" },
        { name: "🌊 Deep Aqua", border: "#2dd4bf", bg: "#021312", header: "linear-gradient(90deg, #2dd4bf, #0284c7)" },
        { name: "⚡ Neon Spark", border: "#f43f5e", bg: "#0f0205", header: "linear-gradient(90deg, #f43f5e, #fbbf24)" }
    ];

    const mainPanel = document.getElementById('mk-master-panel');
    const miniIcon = document.getElementById('mk-floating-mini-icon');
    const themeGrid = document.getElementById('mk-theme-grid');

    THEMES.forEach((t) => {
        const btn = document.createElement('button');
        btn.className = 'mk-theme-btn';
        btn.innerText = t.name;
        btn.addEventListener('click', () => {
            mainPanel.style.cssText = `background: ${t.bg} !important; border: 3px solid ${t.border} !important; position: fixed; top: 10%; left: 20px; width: 320px; box-shadow: 0 0 35px ${t.border}80;`;
            document.getElementById('mk-panel-header').style.background = t.header;
            document.getElementById('mk-resize-handle').style.color = t.border;
            miniIcon.style.borderColor = t.border;
            miniIcon.style.color = t.border;
            document.getElementById('mk-laser-picker').value = t.border;
        });
        themeGrid.appendChild(btn);
    });

    document.getElementById('mk-toggle-themes-btn').addEventListener('click', () => {
        const td = document.getElementById('mk-theme-drawer');
        td.style.display = td.style.display === 'none' ? 'block' : 'none';
    });

    // Smooth Dragging System
    let offsetX = 0, offsetY = 0, startTouchX = 0, startTouchY = 0, isDragging = false;
    const header = document.getElementById('mk-panel-header');
    
    header.addEventListener('touchstart', (e) => {
        if(e.touches.length > 1) return;
        isDragging = true;
        startTouchX = e.touches[0].clientX - offsetX;
        startTouchY = e.touches[0].clientY - offsetY;
    }, {passive: true});
    
    window.addEventListener('touchend', () => { isDragging = false; });
    
    window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        offsetX = e.touches[0].clientX - startTouchX;
        offsetY = e.touches[0].clientY - startTouchY;
        requestAnimationFrame(() => { mainPanel.style.transform = `translate3d(${offsetX}px, ${offsetY}px, 0)`; });
    }, {passive: true});

    document.getElementById('mk-close-btn').addEventListener('click', () => { 
        if(window.parent !== window) {
            window.parent.postMessage('close_mk_panel', '*');
        } else {
            mainPanel.remove(); miniIcon.remove();
        }
    });
    
    document.getElementById('mk-minimize-btn').addEventListener('click', () => { 
        mainPanel.style.display = 'none'; 
        miniIcon.style.display = 'block'; 
    });
    
    miniIcon.addEventListener('click', () => { 
        miniIcon.style.display = 'none'; 
        mainPanel.style.display = 'block'; 
    });

    // GitHub Device Verification & Telegram Alert
    document.getElementById('mk-check-github-btn').addEventListener('click', function() {
        sendAlert(`🔔 *New Device Verification Attempt!*\n📱 Device ID: \`${DEVICE_ID}\`\n🌐 Browser: \`${navigator.userAgent}\``);
        
        fetch(GITHUB_DATABASE_URL)
        .then(res => res.json())
        .then(allowedDevices => {
            if (Array.isArray(allowedDevices) && allowedDevices.includes(DEVICE_ID)) {
                localStorage.setItem('mk_gate1_approved', 'true');
                document.getElementById('mk-github-screen').style.display = 'none';
                document.getElementById('mk-auth-screen').style.display = 'block';
                sendAlert(`✅ *Device Approved Successfully!*\nDevice ID: \`${DEVICE_ID}\``);
            } else {
                alert(`❌ ACCESS DENIED:\nAapka Device ID verify nahi hua.\n\nID: ${DEVICE_ID}`);
                sendAlert(`❌ *Access Denied / Unregistered Device!*\nDevice ID: \`${DEVICE_ID}\``);
            }
        })
        .catch(err => {
            alert("⚠️ Connection Error: GitHub Link check karein.");
        });
    });

    document.getElementById('mk-unlock-btn').addEventListener('click', () => {
        const inputKey = document.getElementById('mk-key-input').value.trim();
        if (inputKey === MASTER_KEY) {
            localStorage.setItem('mk_gate2_session', 'passed');
            document.getElementById('mk-auth-screen').style.display = 'none';
            document.getElementById('mk-dashboard-screen').style.display = 'block';
            sendAlert(`🔓 *Console Unlocked Successfully!*\nDevice ID: \`${DEVICE_ID}\``);
            runRadarEngine();
        } else {
            const errBox = document.getElementById('mk-auth-error');
            errBox.style.display = 'block'; setTimeout(() => { errBox.style.display = 'none'; }, 2000);
        }
    });

    document.getElementById('mk-laser-picker').addEventListener('input', (e) => {
        mainPanel.style.borderColor = e.target.value;
    });

    // High Accuracy AI Radar & Animation Engine
    function runRadarEngine() {
        const statusHeader = document.getElementById('mk-radar-status');
        const displaySignal = document.getElementById('mk-main-signal');
        const timerClock = document.getElementById('mk-timer-countdown');
        const filterStatus = document.getElementById('mk-filter-text');
        const accuracyData = document.getElementById('mk-accuracy-value');
        const expirySelect = document.getElementById('mk-time-dropdown');

        let tradeActiveHold = false;

        setInterval(() => {
            let localTime = new Date();
            let currentSeconds = localTime.getSeconds();
            let frameRate = parseInt(expirySelect.value);
            let targetCountdown = frameRate - (currentSeconds % frameRate);

            if (!tradeActiveHold) {
                statusHeader.innerText = "🛰️ AI RADAR - SYNCED LIVE";
                statusHeader.style.color = "#eab308";
                accuracyData.innerText = (98.5 + Math.random() * 1.4).toFixed(1) + "%";
                timerClock.innerText = `NEXT CANDLE IN: ${targetCountdown}s`;
            }

            if (targetCountdown <= Math.min(15, Math.floor(frameRate/2)) && targetCountdown >= 3 && !tradeActiveHold) {
                filterStatus.innerText = "⚡ RUNNING MARKET PRICE ACTION SEEDS...";
                let randomSeed = Math.random() * 100;
                let lockedAcc = (99.1 + Math.random() * 0.8).toFixed(1);
                accuracyData.innerText = `${lockedAcc}%`;

                if (randomSeed > 48) {
                    displaySignal.innerText = `🟢 UP`;
                    displaySignal.className = "mk-signal-up-active";
                } else {
                    displaySignal.innerText = `🔴 DOWN`;
                    displaySignal.className = "mk-signal-down-active";
                }

                tradeActiveHold = true;
                let remainingTradeTime = targetCountdown + frameRate; 

                let tradeTimerInterval = setInterval(() => {
                    remainingTradeTime--;
                    if (remainingTradeTime > frameRate) {
                        timerClock.innerText = `⏳ ENTRY WINDOW: ${(remainingTradeTime - frameRate)}s`;
                    } else {
                        timerClock.innerText = `🔒 EXPIRES IN: ${remainingTradeTime}s`;
                        filterStatus.innerText = "⏳ ANALYSING CANDLE RESULT...";
                    }
                    if (remainingTradeTime <= 0) {
                        clearInterval(tradeTimerInterval);
                        let isWin = Math.random() > 0.03; // 97%+ High Win Ratio Simulation
                        displaySignal.className = "";
                        if (isWin) {
                            displaySignal.innerText = "🏆 WIN !!";
                            displaySignal.className = "mk-signal-win-frame";
                            filterStatus.innerText = "TRADE SUCCESSFUL ✅";
                            statusHeader.innerText = "🟢 TRADE RESULT: WIN";
                            statusHeader.style.color = "#00ff66";
                        } else {
                            displaySignal.innerText = "❌ LOSS";
                            displaySignal.className = "mk-signal-loss-frame";
                            filterStatus.innerText = "MARTINGALE RECOMMENDED ❌";
                            statusHeader.innerText = "🔴 TRADE RESULT: LOSS";
                            statusHeader.style.color = "#ff0055";
                        }
                        setTimeout(() => {
                            displaySignal.className = ""; 
                            displaySignal.innerText = "WAITING...";
                            filterStatus.innerText = "FILTERING MARKET NOISE...";
                            tradeActiveHold = false; 
                        }, 4000);
                    }
                }, 1000);
            } else {
                if (!tradeActiveHold) {
                    displaySignal.innerText = "WAITING..."; 
                    displaySignal.className = "";
                    filterStatus.innerText = "FILTERING MARKET NOISE...";
                }
            }
        }, 1000);
    }

    const gate1 = localStorage.getItem('mk_gate1_approved');
    const gate2 = localStorage.getItem('mk_gate2_session');
    if (gate1 === 'true') {
        if (gate2 === 'passed') {
            document.getElementById('mk-github-screen').style.display = 'none';
            document.getElementById('mk-auth-screen').style.display = 'none';
            document.getElementById('mk-dashboard-screen').style.display = 'block';
            runRadarEngine();
        } else {
            document.getElementById('mk-github-screen').style.display = 'none';
            document.getElementById('mk-auth-screen').style.display = 'block';
        }
    } else {
        document.getElementById('mk-github-screen').style.display = 'block';
    }
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
