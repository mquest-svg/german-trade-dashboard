import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import yfinance as yf

# Page configuration
st.set_page_config(
    page_title="GermanTradeAnalyst",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    render_sidebar()
    render_header()
    render_daily_opportunities()
    render_technical_analysis()
    render_risk_management()
    render_compliance_footer()

def render_sidebar():
    st.sidebar.title("🇩🇪 GermanTradeAnalyst")
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("Market Selection")
    selected_indices = st.sidebar.multiselect(
        "German Indices to Monitor:",
        options=["DAX", "MDAX", "TecDAX", "SDAX"],
        default=["DAX", "MDAX"]
    )
    
    st.sidebar.subheader("Risk Parameters")
    max_volatility = st.sidebar.slider(
        "Max Volatility %:",
        min_value=5, max_value=30, value=20
    )
    
    min_confidence = st.sidebar.slider(
        "Min Confidence Score:",
        min_value=50, max_value=90, value=70
    )
    
    st.session_state.max_volatility = max_volatility
    st.session_state.min_confidence = min_confidence
    st.session_state.selected_indices = selected_indices
    
    st.sidebar.markdown("---")
    st.sidebar.info("Daily analysis for German markets")

def render_header():
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.title("📈 GermanTradeAnalyst")
        st.markdown("**Low to Medium Risk Trading Opportunities**")
    
    with col2:
        st.metric("DAX Performance", "+0.8%", "Today")
    
    with col3:
        st.metric("Market Sentiment", "Neutral", "-2 points")
    
    st.markdown("---")

def render_daily_opportunities():
    st.header("🎯 Daily Trading Opportunities")
    
    # German stocks with real symbols
    german_stocks = [
        {"Symbol": "SAP.DE", "Name": "SAP SE", "Sector": "Technology"},
        {"Symbol": "ALV.DE", "Name": "Allianz SE", "Sector": "Insurance"},
        {"Symbol": "SIE.DE", "Name": "Siemens AG", "Sector": "Industrial"},
        {"Symbol": "DTE.DE", "Name": "Deutsche Telekom", "Sector": "Telecom"},
        {"Symbol": "BMW.DE", "Name": "BMW AG", "Sector": "Automotive"},
        {"Symbol": "BAS.DE", "Name": "BASF SE", "Sector": "Chemicals"},
        {"Symbol": "BAYN.DE", "Name": "Bayer AG", "Sector": "Pharmaceuticals"},
        {"Symbol": "AIR.DE", "Name": "Airbus SE", "Sector": "Aerospace"},
        {"Symbol": "DBK.DE", "Name": "Deutsche Bank", "Sector": "Banking"},
        {"Symbol": "VOW3.DE", "Name": "Volkswagen AG", "Sector": "Automotive"}
    ]
    
    # Display stock opportunities
    for stock in german_stocks[:5]:  # Show first 5
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            
            with col1:
                st.subheader(f"{stock['Symbol']}")
                st.write(f"**{stock['Name']}**")
                st.caption(f"Sector: {stock['Sector']}")
            
            with col2:
                # Simulated price data
                price = np.random.uniform(50, 300)
                st.metric("Current Price", f"€{price:.2f}")
                
                change = np.random.uniform(-2, 3)
                change_color = "green" if change > 0 else "red"
                st.write(f"Change: :{change_color}[{change:+.1f}%]")
            
            with col3:
                volatility = np.random.uniform(8, 25)
                risk = "Low" if volatility < 15 else "Medium" if volatility < 20 else "High"
                risk_color = "green" if risk == "Low" else "orange" if risk == "Medium" else "red"
                
                st.write(f"**Volatility:** {volatility:.1f}%")
                st.write(f"**Risk:** :{risk_color}[{risk}]")
            
            with col4:
                confidence = np.random.randint(60, 95)
                confidence_color = "green" if confidence >= 80 else "orange" if confidence >= 70 else "red"
                
                st.markdown(f"**Confidence:** :{confidence_color}[{confidence}%]")
                st.progress(confidence/100)
                
                if st.button("Analyze", key=stock['Symbol']):
                    st.session_state.selected_stock = stock['Symbol']
            
            st.markdown("---")

def render_technical_analysis():
    st.header("📊 Technical Analysis")
    
    # Stock selector
    german_symbols = ["SAP.DE", "ALV.DE", "SIE.DE", "DTE.DE", "BMW.DE", "BAS.DE"]
    selected_symbol = st.selectbox("Select stock for analysis:", german_symbols)
    
    if selected_symbol:
        # Create sample technical chart
        st.subheader(f"Technical Analysis - {selected_symbol}")
        
        # Generate sample price data
        dates = pd.date_range(start='2024-01-01', periods=60, freq='D')
        base_price = 100
        
        # Simulate stock price movement
        returns = np.random.normal(0.001, 0.02, len(dates))
        prices = base_price * (1 + returns).cumprod()
        
        # Create interactive chart
        fig = go.Figure()
        
        # Price line
        fig.add_trace(go.Scatter(
            x=dates, y=prices,
            mode='lines',
            name='Price',
            line=dict(color='#1f77b4', width=2)
        ))
        
        # Moving averages
        fig.add_trace(go.Scatter(
            x=dates, y=pd.Series(prices).rolling(20).mean(),
            mode='lines',
            name='SMA 20',
            line=dict(color='orange', width=1.5)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates, y=pd.Series(prices).rolling(50).mean(),
            mode='lines', 
            name='SMA 50',
            line=dict(color='red', width=1.5)
        ))
        
        fig.update_layout(
            title=f"{selected_symbol} - Price Chart with Moving Averages",
            xaxis_title="Date",
            yaxis_title="Price (€)",
            height=500,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Technical indicators in columns
        st.subheader("Technical Indicators")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            rsi = np.random.randint(30, 70)
            rsi_status = "Oversold" if rsi < 30 else "Overbought" if rsi > 70 else "Neutral"
            rsi_color = "red" if rsi < 30 else "green" if rsi > 70 else "orange"
            st.metric("RSI", f"{rsi}", rsi_status)
            st.progress(rsi/100)
        
        with col2:
            macd = np.random.uniform(-2, 2)
            macd_status = "Bullish" if macd > 0.5 else "Bearish" if macd < -0.5 else "Neutral"
            macd_color = "green" if macd > 0.5 else "red" if macd < -0.5 else "orange"
            st.metric("MACD", f"{macd:+.2f}", macd_status)
        
        with col3:
            volatility = np.random.uniform(10, 25)
            vol_status = "High" if volatility > 20 else "Low" if volatility < 15 else "Medium"
            st.metric("Volatility", f"{volatility:.1f}%", vol_status)
        
        with col4:
            trend = np.random.choice(["🟢 Strong Up", "↗️ Mild Up", "➡️ Sideways", "↘️ Mild Down", "🔻 Strong Down"])
            st.metric("Trend", trend)

def render_risk_management():
    st.header("🛡️ Risk Management Toolkit")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Position Size Calculator")
        
        portfolio = st.number_input("Portfolio Size (€):", min_value=1000, value=25000, step=1000)
        risk_percent = st.slider("Risk per Trade (%):", 0.5, 5.0, 2.0, 0.5)
        entry_price = st.number_input("Entry Price (€):", min_value=1.0, value=100.0, step=0.1)
        stop_loss = st.number_input("Stop Loss (€):", min_value=1.0, value=95.0, step=0.1)
        
        if st.button("Calculate Position"):
            risk_amount = portfolio * (risk_percent / 100)
            loss_per_share = entry_price - stop_loss
            
            if loss_per_share > 0:
                shares = risk_amount / loss_per_share
                position_value = shares * entry_price
                
                st.success(f"**Position Size:** {shares:.0f} shares")
                st.success(f"**Investment:** €{position_value:,.2f}")
                st.info(f"**Risk:** €{risk_amount:,.2f} ({risk_percent}% of portfolio)")
            else:
                st.error("Stop loss must be below entry price")
    
    with col2:
        st.subheader("Stop-Loss Calculator")
        
        current_price = st.number_input("Current Price (€):", value=150.0, step=0.1, key="curr_price")
        risk_reward = st.selectbox("Risk-Reward Ratio:", [1.5, 2.0, 2.5, 3.0, 3.5])
        stop_loss_pct = st.slider("Stop-Loss Distance (%):", 1.0, 10.0, 5.0, 0.5)
        
        stop_loss_price = current_price * (1 - stop_loss_pct/100)
        loss_per_share = current_price - stop_loss_price
        take_profit_price = current_price + (loss_per_share * risk_reward)
        
        st.metric("Stop-Loss Price", f"€{stop_loss_price:.2f}")
        st.metric("Take-Profit Price", f"€{take_profit_price:.2f}")
        st.metric("Risk-Reward Ratio", f"1:{risk_reward}")
        
        # Visual representation
        st.info(f"**For every €1 risked, potential reward: €{risk_reward}**")

def render_compliance_footer():
    st.markdown("---")
    
    st.warning("""
    **⚠️ RISIKOHINWEIS NACH § 64 ABS. 4 BÖRSG:**
    Die bereitgestellten Informationen stellen keine Anlageberatung dar. Kapitalanlagen sind mit Risiken verbunden. 
    Der Totalverlust des eingesetzten Kapitals ist möglich. Bitte konsultieren Sie einen qualifizierten Finanzberater.
    """)
    
    st.info("""
    **🔒 DATENSCHUTZ:** Diese Anwendung verarbeitet Daten gemäß DSGVO. 
    **📊 DATENQUELLEN:** Yahoo Finance, Simulierte Daten
    **ℹ️ HINWEIS:** Diese Demo zeigt simulierte Daten zu Schulungszwecken.
    **🎯 ZWECK:** Persönliche Analyseunterstützung, keine Anlageempfehlung.
    """)
    
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | GermanTradeAnalyst v1.0")

if __name__ == "__main__":
    main()
