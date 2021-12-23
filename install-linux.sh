# 

install() {
    if hash ipscan 2>/dev/null; then
        echo "[*] Angry IP Scanner Installed\n"
        ipscan -h
    else
        echo "Installing Angry IP Commandline Utility"
        sudo apt update && sudo apt upgrade -y
        sudo dpkg -i ./core/ipscan_3.7.6_all.deb
        sudo apt -f install
    fi
}

install 