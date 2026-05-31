# XRPL AI Scout - Main Application Entry Point
# Montana LLC - XRP Institutional Intelligence Monitor
# Version 1.0 - MVP Architecture

import os
from xrpl_monitor import XRPLMonitor
from signal_analyzer import SignalAnalyzer
from portfolio_tracker import PortfolioTracker
from alert_system import AlertSystem

def main():
    """
    XRPL AI Scout Main Application
    
    Monitors institutional signals around XRP ecosystem
    Analyzes DTCC/Stellar developments using tiered credibility framework
    Tracks portfolio performance in XRP terms
    Delivers structured intelligence to XRP investors
    """
    
    print("XRPL AI Scout - Initializing...")
    
    # Initialize core components
    monitor = XRPLMonitor()
    analyzer = SignalAnalyzer()
    tracker = PortfolioTracker()
    alerts = AlertSystem()
    
    # Start monitoring loop
    monitor.start()
    print("Monitoring active - watching for Tier 1 institutional signals")

if __name__ == "__main__":
    main()
