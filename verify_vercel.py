"""
Vercel Deployment Verification Script
Checks that all required components are properly configured for Vercel deployment
"""
import sys
import os
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if Path(filepath).exists():
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ MISSING {description}: {filepath}")
        return False

def check_file_content(filepath, required_strings, description):
    """Check if file contains required strings"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing = []
        for req in required_strings:
            if req not in content:
                missing.append(req)
        
        if not missing:
            print(f"✓ {description}: All required content found")
            return True
        else:
            print(f"✗ {description}: Missing {missing}")
            return False
    except Exception as e:
        print(f"✗ Error reading {filepath}: {e}")
        return False

def main():
    print("=" * 70)
    print("VERCEL DEPLOYMENT VERIFICATION")
    print("=" * 70)
    print()
    
    checks = []
    
    # Check essential files exist
    print("1. Checking essential files...")
    print("-" * 70)
    checks.append(check_file_exists("vercel.json", "Vercel config"))
    checks.append(check_file_exists("runtime.txt", "Python runtime"))
    checks.append(check_file_exists("api/index.py", "API entry point"))
    checks.append(check_file_exists("api/requirements.txt", "API dependencies"))
    checks.append(check_file_exists("package.json", "Frontend package"))
    print()
    
    # Check runtime.txt
    print("2. Checking Python runtime...")
    print("-" * 70)
    checks.append(check_file_content("runtime.txt", ["python-3.13"], "Python 3.13 specified"))
    print()
    
    # Check vercel.json
    print("3. Checking Vercel configuration...")
    print("-" * 70)
    checks.append(check_file_content("vercel.json", [
        "api/index.py",
        "@vercel/python",
        "python3.13",
        "vite"
    ], "Vercel config"))
    print()
    
    # Check api/requirements.txt doesn't have problematic packages
    print("4. Checking API dependencies...")
    print("-" * 70)
    try:
        with open("api/requirements.txt", 'r') as f:
            reqs = f.read()
        
        if "gunicorn" in reqs.lower():
            print("⚠ WARNING: gunicorn found (not needed for Vercel)")
            checks.append(False)
        else:
            print("✓ No gunicorn (correct for Vercel)")
            checks.append(True)
        
        required_packages = ["Flask", "Flask-CORS", "pandas", "numpy", "openpyxl"]
        for pkg in required_packages:
            if pkg.lower() in reqs.lower():
                print(f"✓ {pkg} found")
            else:
                print(f"✗ MISSING: {pkg}")
                checks.append(False)
    except Exception as e:
        print(f"✗ Error checking requirements: {e}")
        checks.append(False)
    print()
    
    # Check api/index.py exports Flask app
    print("5. Checking Flask app export...")
    print("-" * 70)
    checks.append(check_file_content("api/index.py", [
        "app = Flask(__name__)",
        "from flask import",
        "CORS(app)"
    ], "Flask app properly configured"))
    print()
    
    # Check package.json build script
    print("6. Checking frontend build configuration...")
    print("-" * 70)
    checks.append(check_file_content("package.json", [
        '"build"',
        'vite build'
    ], "Vite build script"))
    print()
    
    # Summary
    print("=" * 70)
    passed = sum(checks)
    total = len(checks)
    print(f"VERIFICATION RESULT: {passed}/{total} checks passed")
    print("=" * 70)
    print()
    
    if passed == total:
        print("✓ ALL CHECKS PASSED - Ready for Vercel deployment!")
        print()
        print("Next steps:")
        print("1. git add .")
        print("2. git commit -m 'Prepare Vercel deployment'")
        print("3. git push origin main")
        print("4. Import repository in Vercel dashboard")
        return 0
    else:
        print("✗ SOME CHECKS FAILED - Please fix issues above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
