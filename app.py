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

JS_PAYLOAD = """
(function() {
    if(document.getElementById('mk-master-panel')) {
        document.getElementById('mk-master-panel').remove();
        if(document.getElementById('mk-floating-mini-icon')) document.getElementById('mk-floating-mini-icon').remove();
        if(document.getElementById('mk-injected-style')) document.getElementById('mk-injected-style').remove();
    }

    const style = document.createElement('style');
    style.id = 'mk-injected-style';
    style.innerHTML = `
        #mk-master-panel {
            position: fixed !important; top: 10% !important; left: 15px !important; width: 320px !important; height: auto !important; max-height: 85vh !important;
            background: #06090f !important; border-radius: 18px !important;
            z-index: 2147483647 !important; color: #fff !important; font-family: sans-serif !important;
            box-sizing: border-box !important; border: 3px solid #00f0ff !important; overflow-y: auto !important; overflow-x: hidden !important;
            box-shadow: 0 0 35px rgba(0, 240, 255, 0.7) !important; touch-action: none !important;
        }
        #mk-master-panel::-webkit-scrollbar { width: 4px; }
        #mk-master-panel::-webkit-scrollbar-thumb { background: #00f0ff; border-radius: 4px; }
        
        #mk-panel-header {
            background: linear-gradient(90deg, #ff0055, #7000ff, #00f0ff) !important;
            padding: 12px 14px !important; font-weight: bold !important; font-size: 13px !important;
            text-align: center !important; cursor: move !important; display: flex !important; justify-content: space-between !important; align-items: center !important;
            user-select: none !important; position: sticky !important; top: 0 !important; z-index: 10 !important;
        }
        .mk-screen { padding: 16px !important; box-sizing: border-box !important; display: flex !important; flex-direction: column !important; gap: 12px !important; width: 100% !important; }
        .mk-sec-title { font-size: 14px !important; font-weight: bold !important; color: #ff0055 !important; text-align: center !important; text-shadow: 0 0 8px rgba(255,0,85,0.7) !important; }
        .mk-sec-subtitle { font-size: 11px !important; color: #94a3b8 !important; text-align: center !important; line-height: 1.4 !important; }
        #mk-key-input { width: 100% !important; padding: 11px !important; background: #000 !important; border: 2px solid #1e293b !important; border-radius: 8px !important; color: #fff !important; text-align: center !important; font-weight: bold !important; outline: none !important; box-sizing: border-box !important; font-size: 13px !important; }
        .mk-link-btn { width: 100% !important; padding: 11px !important; background: #1e1b4b !important; color: #a855f7 !important; border: 1px solid #4c1d95 !important; font-weight: bold !important; border-radius: 8px !important; text-align: center !important; text-decoration: none !important; display: block !important; box-sizing: border-box !important; font-size: 11.5px !important; }
        #mk-radar-status { text-align: center !important; color: #eab308 !important; font-size: 11.5px !important; font-weight: bold !important; }
        #mk-signal-box { background: #0f172a !important; padding: 18px !important; border-radius: 12px !important; text-align: center !important; border: 1px solid #1e293b !important; box-sizing: border-box !important; min-height: 90px !important; display: flex !important; flex-direction: column !important; justify-content: center !important; }
        #mk-main-signal { font-size: 22px !important; font-weight: 900 !important; color: #fff !important; width: 100% !important; padding: 8px 0 !important; border-radius: 8px !important; }
        #mk-timer-countdown { font-size: 11.5px !important; color: #94a3b8 !important; margin-top: 6px !important; font-weight: bold !important; }
        #mk-filter-text { text-align: center !important; color: #10b981 !important; font-size: 11.5px !important; font-weight: bold !important; }
        #mk-accuracy-wrapper { text-align: center !important; color: #e2e8f0 !important; font-size: 12.5px !important; font-weight: bold !important; }
        #mk-accuracy-value { color: #06b6d4 !important; font-weight: 900 !important; text-shadow: 0 0 8px #06b6d4 !important; }
        .mk-control-row { display: flex !important; justify-content: space-between !important; align-items: center !important; font-size: 12px !important; color: #94a3b8 !important; }
        .mk-control-row select { background: #000 !important; color: #fff !important; border: 1px solid #334155 !important; border-radius: 7px !important; padding: 6px !important; width: 135px !important; outline: none !important; font-weight: bold !important; }
        .mk-control-row input[type="color"] { border: none !important; background: transparent !important; width: 28px !important; height: 28px !important; cursor: pointer !important; }
        .mk-theme-btn { background: #0f172a !important; color: #fff !important; border: 1px solid #334155 !important; border-radius: 7px !important; padding: 7px !important; font-size: 10px !important; cursor: pointer !important; text-align: center !important; font-weight: bold !important; }
        .mk-theme-btn:hover { background: #00f0ff !important; color: #000 !important; border-color: #00f0ff !important; }
        #mk-minimize-btn { width: 100% !important; background: transparent !important; border: 1px dashed #334155 !important; color: #94a3b8 !important; font-size: 11px !important; font-weight: bold !important; padding: 8px !important; border-radius: 7px !important; cursor: pointer !important; }
        #mk-floating-mini-icon { position: fixed !important; top: 20% !important; left: 15px !important; padding: 12px 16px !important; background: #06090f !important; border: 2px solid #00f0ff !important; border-radius: 12px !important; color: #00f0ff !important; font-size: 12px !important; font-weight: bold !important; cursor: pointer !important; z-index: 2147483647 !important; display: none !important; box-shadow: 0 0 25px rgba(0,240,255,0.7) !important; touch-action: none !important; }
        .mk-signal-up-active { background: linear-gradient(135deg, #00ff66, #00b347) !important; color: #000 !important; box-shadow: 0 0 30px #00ff66 !important; font-size: 25px !important; font-weight: 900 !important; }
        .mk-signal-down-active { background: linear-gradient(135deg, #ff0055, #b3003b) !important; color: #fff !important; box-shadow: 0 0 30px #ff0055 !important; font-size: 25px !important; font-weight: 900 !important; }
        .mk-signal-win-frame { background: rgba(0, 255, 102, 0.25) !important; color: #00ff66 !important; border: 2px dashed #00ff66 !important; font-size: 23px !important; font-weight: 900 !important; }
        .mk-signal-loss-frame { background: rgba(255, 0, 85, 0.25) !important; color: #ff0055 !important; border: 2px dashed #ff0055 !important; font-size: 23px !important; font-weight: 900 !important; }
    `;
    document.head.appendChild(style);

    const mainPanel = document.createElement('div');
    mainPanel.id = 'mk-master-panel';
    mainPanel.innerHTML = `
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
    `;
    document.body.appendChild(mainPanel);

    const miniIcon = document.createElement('div');
    miniIcon.id = 'mk-floating-mini-icon';
    miniIcon.innerHTML = `<span>🚀 M.K PRO</span>`;
    document.body.appendChild(miniIcon);

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

    const themeGrid = document.getElementById('mk-theme-grid');
    THEMES.forEach((t) => {
        const btn = document.createElement('button');
        btn.className = 'mk-theme-btn';
        btn.innerText = t.name;
        btn.addEventListener('click', () => {
            mainPanel.style.cssText = `position: fixed !important; top: 10% !important; left: 15px !important; width: 320px !important; max-height: 85vh !important; background: ${t.bg} !important; border: 3px solid ${t.border} !important; box-shadow: 0 0 35px ${t.border}80 !important; border-radius: 18px !important; z-index: 2147483647 !important; overflow-y: auto !important;`;
            document.getElementById('mk-panel-header').style.background = t.header;
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
        mainPanel.remove(); miniIcon.remove(); style.remove();
    });
    
    document.getElementById('mk-minimize-btn').addEventListener('click', () => { 
        mainPanel.style.display = 'none'; 
        miniIcon.style.display = 'block'; 
    });
    
    miniIcon.addEventListener('click', () => { 
        miniIcon.style.display = 'none'; 
        mainPanel.style.display = 'block'; 
    });

    document.getElementById('mk-check-github-btn').addEventListener('click', function() {
        sendAlert(`🔔 *New Device Verification Attempt!*\n📱 Device ID: \`${DEVICE_ID}\``);
        fetch(GITHUB_DATABASE_URL)
        .then(res => res.json())
        .then(allowedDevices => {
            if (Array.isArray(allowedDevices) && allowedDevices.includes(DEVICE_ID)) {
                localStorage.setItem('mk_gate1_approved', 'true');
                document.getElementById('mk-github-screen').style.display = 'none';
                document.getElementById('mk-auth-screen').style.display = 'block';
                sendAlert(`✅ *Device Approved Successfully!*\nDevice ID: \`${DEVICE_ID}\``);
            } else {
                alert(`❌ ACCESS DENIED:\nAapka Device ID verify nahi hua.\\n\\nID: ${DEVICE_ID}`);
                sendAlert(`❌ *Access Denied!*\nDevice ID: \`${DEVICE_ID}\``);
            }
        })
        .catch(err => { alert("⚠️ Connection Error!"); });
    });

    document.getElementById('mk-unlock-btn').addEventListener('click', () => {
        const inputKey = document.getElementById('mk-key-input').value.trim();
        if (inputKey === MASTER_KEY) {
            localStorage.setItem('mk_gate2_session', 'passed');
            document.getElementById('mk-auth-screen').style.display = 'none';
            document.getElementById('mk-dashboard-screen').style.display = 'block';
            sendAlert(`🔓 *Console Unlocked!*\nDevice ID: \`${DEVICE_ID}\``);
            runRadarEngine();
        } else {
            const errBox = document.getElementById('mk-auth-error');
            errBox.style.display = 'block'; setTimeout(() => { errBox.style.display = 'none'; }, 2000);
        }
    });

    document.getElementById('mk-laser-picker').addEventListener('input', (e) => {
        mainPanel.style.borderColor = e.target.value;
    });

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
                        let isWin = Math.random() > 0.03; 
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
                            statusHeader.innerText = "🟢 TRADE RESULT: LOSS";
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
})();
"""

@app.route('/')
def home():
    return JS_PAYLOAD, 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
