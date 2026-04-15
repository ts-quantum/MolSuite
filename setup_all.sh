#!/bin/bash
# MoleculeSuite Installer (MolVista & OrbVista)

APP_DIR="$(cd "$(dirname "$0")" && pwd)"

#edit path according to your specific settings
#path to *.desktop scripts
BIN_DIR="$HOME/.local/share/applications"

echo "Installing MoleculeSuite Shortcuts..."

# crearte desktop launcher
create_launcher() {
    local name=$1
    local exec_file=$2
    local icon_path=$3
    local desktop_file="$BIN_DIR/${name,,}.desktop"

    cat <<EOF > "$desktop_file"
[Desktop Entry]
Version=1.0
Type=Application
Name=$name
Exec=$APP_DIR/$exec_file
Icon=$APP_DIR/$icon_path
Terminal=false
Categories=Science;Visualization;
EOF
    chmod +x "$desktop_file"
}

# 1. MolVista
create_launcher "MolVista" "MolVista_run" "MolVista/modules/icon.png"

# 2. OrbVista
create_launcher "OrbVista" "OrbVista_run" "OrbVista/modules/icon.png"

update-desktop-database ~/.local/share/applications/ 2>/dev/null
echo "Done! Both apps are now available in your menu."
