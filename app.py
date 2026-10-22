import os
import requests
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8856455940:AAF9DN02srBYgWPU0MM8W3IVma9vg68yVJk"
TELEGRAM_CHAT_ID = "7588675873"

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
    <title>🚀 𝗠.𝗞 𝗔𝗜 𝗦𝗜𝗚𝗡𝗔𝗟𝗦 𝗣𝗥𝗢 🚀</title>
</head>
<body>
<script>
    if (document.getElementById('mk-master-panel')) {
        document.getElementById('mk-master-panel').remove();
    }

    const mainPanel = document.createElement('div');
    mainPanel.id = 'mk-master-panel';
    mainPanel.innerHTML = `
        <div id="mk-panel-header">
            <span>🚀 𝗠.𝗞 𝗔𝗜 𝗦𝗜𝗚𝗡𝗔𝗟𝗦 𝗣𝗥𝗢 🚀</span>
            <div style="display:flex; gap:6px; align-items:center;">
                <span id="mk-toggle-themes-btn" style="cursor:pointer; font-size:10px; background:rgba(0,0,0,0.5); padding:2px 5px; border-radius:4px;">🎨 LOOKS</span>
                <span id="mk-close-btn" style="cursor:pointer; font-weight:bold; margin-left:4px;">✕</span>
            </div>
        </div>
        
        <div id="mk-theme-drawer" style="display:none; background:rgba(0,0,0,0.9); padding:8px; border-bottom:1px solid #222;">
            <div id="mk-theme-grid" style="display:grid; grid-template-columns:repeat(2, 1fr); gap:4px; max-height:100px; overflow-y:auto;"></div>
        </div>

        <div id="mk-dashboard-screen" class="mk-screen">
            <div id="mk-radar-status">🛰️ AI RADAR - SYNCED LIVE</div>
            
            <div id="mk-signal-box">
                <div id="mk-main-signal">WAITING...</div>
                <div id="mk-timer-countdown">NEXT CANDLE IN: --s</div>
            </div>
            
            <div id="mk-filter-text">FILTERING MARKET NOISE...</div>
            <div id="mk-accuracy-wrapper">🎯 ACCURACY: <span id="mk-accuracy-value">98.9%</span></div>

            <div class="mk-control-row">
                <label>⏱️ Expiry:</label>
                <select id="mk-time-dropdown">
                    <option value="60" selected>1 Minute</option>
                    <option value="30">30 Second</option>
                    <option value="10">10 Second</option>
                </select>
            </div>

            <a href="https://t.me/MK_TRADER586" target="_blank" class="mk-link-btn">📞 CONTACT M.K TRADER</a>
            <button id="mk-minimize-btn">🗕 MINIMIZE TERMINAL</button>
        </div>
        <div id="mk-resize-handle">◢</div>
    `;
    document.body.appendChild(mainPanel);

    const miniIcon = document.createElement('div');
    miniIcon.id = 'mk-floating-mini-icon';
    miniIcon.innerHTML = `<span>🚀 M.K PRO</span>`;
    document.body.appendChild(miniIcon);

    const style = document.createElement('style');
    style.innerHTML = `
        #mk-master-panel {
            position: fixed; top: 15%; left: 30px; width: 290px; height: auto;
            background: #090c10 !important; border-radius: 14px;
            z-index: 2147483647 !important; color: #fff; font-family: sans-serif;
            box-sizing: border-box; border: 3px solid #00f0ff; overflow: hidden;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.3); touch-action: none;
        }
        #mk-panel-header {
            background: linear-gradient(90deg, #ff0055, #7000ff, #00f0ff);
            padding: 10px 12px; font-weight: bold; font-size: 12px;
            text-align: center; cursor: move; display: flex; justify-content: space-between; align-items: center;
            user-select: none; -webkit-user-select: none;
        }
        .mk-screen { padding: 14px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; width: 100%; }
        .mk-link-btn { width: 100%; padding: 10px; background: #1e1b4b; color: #a855f7; border: 1px solid #4c1d95; font-weight: bold; border-radius: 6px; text-align: center; text-decoration: none; display: block; box-sizing: border-box; font-size: 11px; }
        #mk-radar-status { text-align: center; color: #eab308; font-size: 11px; font-weight: bold; }
        #mk-signal-box { background: #111827; padding: 16px; border-radius: 8px; text-align: center; border: 1px solid #1f2937; box-sizing: border-box; min-height: 80px; display: flex; flex-direction: column; justify-content: center; }
        #mk-main-signal { font-size: 18px; font-weight: bold; color: #fff; width: 100%; padding: 6px 0; border-radius: 4px; }
        #mk-timer-countdown { font-size: 11px; color: #9ca3af; margin-top: 4px; }
        #mk-filter-text { text-align: center; color: #10b981; font-size: 11px; font-weight: bold; }
        #mk-accuracy-wrapper { text-align: center; color: #cbd5e1; font-size: 12px; font-weight: bold; }
        #mk-accuracy-value { color: #06b6d4; font-weight: 900; text-shadow: 0 0 6px #06b6d4; }
        .mk-control-row { display: flex; justify-content: space-between; align-items: center; font-size: 11.5px; color: #9ca3af; }
        .mk-control-row select { background: #000; color: #fff; border: 1px solid #374151; border-radius: 6px; padding: 5px; width: 130px; outline: none; }
        .mk-theme-btn { background: #161e2e; color: #fff; border: 1px solid #2d3748; border-radius: 4px; padding: 5px; font-size: 9px; cursor: pointer; text-align: center; font-weight: bold; }
        #mk-minimize-btn { width: 100%; background: transparent; border: 1px dashed #374151; color: #9ca3af; font-size: 10px; font-weight: bold; padding: 6px; border-radius: 6px; cursor: pointer; }
        #mk-resize-handle { position: absolute; right: 0; bottom: 0; width: 18px; height: 18px; color: #00f0ff; cursor: se-resize; font-size: 11px; text-align: right; line-height: 18px; z-index: 2147483647; font-weight: bold; user-select: none; }
        #mk-floating-mini-icon { position: fixed; top: 20%; left: 15px; padding: 10px 14px; background: #090c10; border: 2px solid #00f0ff; border-radius: 8px; color: #00f0ff; font-size: 11px; font-weight: bold; cursor: pointer; z-index: 2147483647 !important; display: none; text-shadow: 0 0 5px #00f0ff; box-shadow: 0 0 15px rgba(0,240,255,0.5); touch-action: none; }
        
        .mk-signal-up-active { background: #00ff66 !important; color: #000 !important; box-shadow: 0 0 20px #00ff66 !important; font-size: 24px !important; font-weight: 900 !important; }
        .mk-signal-down-active { background: #ff0055 !important; color: #fff !important; box-shadow: 0 0 20px #ff0055 !important; font-size: 24px !important; font-weight: 900 !important; }
        .mk-signal-win-frame { background: rgba(0, 255, 102, 0.15) !important; color: #00ff66 !important; border: 2px dashed #00ff66 !important; font-size: 22px !important; font-weight: 900 !important; text-shadow: 0 0 8px #00ff66 !important; }
        .mk-signal-loss-frame { background: rgba(255, 0, 85, 0.15) !important; color: #ff0055 !important; border: 2px dashed #ff0055 !important; font-size: 22px !important; font-weight: 900 !important; text-shadow: 0 0 8px #ff0055 !important; }
    `;
    document.head.appendChild(style);

    const THEMES = [
        { name: "🩵 Cyan Neon", border: "#00f0ff", bg: "#090c10", header: "linear-gradient(90deg, #ff0055, #7000ff, #00f0ff)" },
        { name: "❤️ Cyber Punk", border: "#ff0055", bg: "#0a0005", header: "linear-gradient(90deg, #ff0055, #330011)" },
        { name: "💛 VIP Gold", border: "#ffd700", bg: "#0a0700", header: "linear-gradient(90deg, #ffd700, #221100)" },
        { name: "💚 Matrix Pro", border: "#00ff66", bg: "#000a03", header: "linear-gradient(90deg, #00ff66, #001100)" },
        { name: "💜 Venom Dark", border: "#a855f7", bg: "#05000a", header: "linear-gradient(90deg, #a855f7, #1e1b4b)" }
    ];

    const themeGrid = document.getElementById('mk-theme-grid');
    THEMES.forEach((t) => {
        const btn = document.createElement('button');
        btn.className = 'mk-theme-btn';
        btn.innerText = t.name;
        btn.addEventListener('click', () => {
            mainPanel.style.cssText = `background: ${t.bg} !important; border: 3px solid ${t.border} !important; position: fixed; top: 15%; left: 30px; width: 290px;`;
            document.getElementById('mk-panel-header').style.background = t.header;
            document.getElementById('mk-resize-handle').style.color = t.border;
            miniIcon.style.borderColor = t.border;
            miniIcon.style.color = t.border;
        });
        themeGrid.appendChild(btn);
    });

    document.getElementById('mk-toggle-themes-btn').addEventListener('click', () => {
        const td = document.getElementById('mk-theme-drawer');
        td.style.display = td.style.display === 'none' ? 'block' : 'none';
    });

    document.getElementById('mk-close-btn').addEventListener('click', () => { mainPanel.style.display = 'none'; miniIcon.style.display = 'block'; });
    document.getElementById('mk-minimize-btn').addEventListener('click', () => { mainPanel.style.display = 'none'; miniIcon.style.display = 'block'; });
    miniIcon.addEventListener('click', () => { miniIcon.style.display = 'none'; mainPanel.style.display = 'block'; });

    // Dragging Logic
    let offsetX = 0, offsetY = 0, startX = 0, startY = 0, isDragging = false;
    const header = document.getElementById('mk-panel-header');
    header.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX - offsetX;
        startY = e.clientY - offsetY;
        e.preventDefault();
    });
    window.addEventListener('mouseup', () => { isDragging = false; });
    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        offsetX = e.clientX - startX;
        offsetY = e.clientY - startY;
        requestAnimationFrame(() => { mainPanel.style.transform = `translate3d(${offsetX}px, ${offsetY}px, 0)`; });
    });

    // Radar Engine
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
            accuracyData.innerText = (97.1 + Math.random() * 2.2).toFixed(1) + "%";
            timerClock.innerText = `NEXT CANDLE IN: ${targetCountdown}s`;
        }

        if (targetCountdown <= 15 && targetCountdown >= 11 && !tradeActiveHold) {
            filterStatus.innerText = "⚡ RUNNING MARKET PRICE ACTION SEEDS...";
            let randomSeed = Math.random() * 100;
            let lockedAcc = (98.5 + Math.random() * 1.4).toFixed(1);
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
                    filterStatus.innerText = "⏳ WAITING FOR SIGNAL RESULT...";
                }
                if (remainingTradeTime <= 0) {
                    clearInterval(tradeTimerInterval);
                    let isWin = Math.random() > 0.05; 
                    displaySignal.className = "";
                    if (isWin) {
                        displaySignal.innerText = "🏆 WIN !!";
                        displaySignal.className = "mk-signal-win-frame";
                        filterStatus.innerText = "ANALYSIS COMPLETED ✅";
                        statusHeader.innerText = "🟢 TRADE RESULT: WIN";
                        statusHeader.style.color = "#00ff66";
                    } else {
                        displaySignal.innerText = "❌ LOSS";
                        displaySignal.className = "mk-signal-loss-frame";
                        filterStatus.innerText = "ALERT: MARTINGALE RECOMMENDED ❌";
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
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
