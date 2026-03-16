# ... (same Flask + LoginManager setup)
@app.route('/chat', methods=['POST'])
@login_required
def chat():
    query = request.json['query']
    is_premium = current_user.is_premium
    
    if 'trade' in query.lower() or 'profit' in query.lower() or 'arbitrage' in query.lower():
        # Auto-run profitable simulation
        data = apis.get_crypto_data('ethereum')  # or parse ticker
        pred = models.predict_price(data)
        current = data['price'].iloc[-1] if not data.empty else 3000
        sim = models.simulate_profitable_trade(query, pred, current, is_premium)
        grok_resp = models.grok_predict(query, sim, is_premium)
    else:
        # normal flow
        ...
    
    return jsonify({'response': grok_resp})