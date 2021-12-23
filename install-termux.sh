# 

install() {
    if hash ipscan 2>/dev/null; then
        echo "[*] Angry IP Scanner Installed\n"
        ipscan -h
    else
        echo "Installing Angry IP Commandline Utility"
        apt update && sudo apt upgrade -y
        dpkg -i ./core/ipscan_3.7.6_all.deb
        apt -f install
    fi
}

install 