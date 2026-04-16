from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/tradingview-alert', methods=['POST'])
def tradingview_alert():
    try:
        data = request.json
        print(f"Received alert: {data}")
        
        action = data.get('action', 'buy')
        symbol = data.get('symbol', 'BTCUSDT')
        amount = float(data.get('amount', 50))
        strategy = data.get('strategy', 'TradingView Alert')
        
        print(f"EXECUTING TRADE: {action} {symbol} ${amount} - {strategy}")
        
        return jsonify({
            "status": "success",
            "message": f"{action.upper()} signal received for {symbol}",
            "data": data
        }), 200
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "message": "Bot is running!"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
