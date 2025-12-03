"""
Test script for the Flask API endpoints
"""
import requests
import sys
import time

# Wait a moment for server to be ready
time.sleep(2)

BASE_URL = "http://localhost:5000"

def test_health():
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✓ Health Check: {response.status_code}")
        print(f"  Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"✗ Health Check Failed: {e}")
        return False

def test_root():
    """Test the root endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✓ Root Endpoint: {response.status_code}")
        print(f"  Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"✗ Root Endpoint Failed: {e}")
        return False

def test_process_file_no_file():
    """Test process-file endpoint without file (should fail gracefully)"""
    try:
        response = requests.post(f"{BASE_URL}/process-file")
        print(f"✓ Process File (no file): {response.status_code}")
        result = response.json()
        print(f"  Response: {result}")
        # Should return error but not crash
        return response.status_code == 400
    except Exception as e:
        print(f"✗ Process File Test Failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Testing Flask API Endpoints")
    print("=" * 60)
    
    tests = [
        ("Health Check", test_health),
        ("Root Endpoint", test_root),
        ("Process File (no file)", test_process_file_no_file),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\nTesting: {name}")
        print("-" * 40)
        results.append(test_func())
        print()
    
    print("=" * 60)
    print(f"Results: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)
    
    sys.exit(0 if all(results) else 1)
