#!/bin/bash

# Hata durumunda betiği durdur
set -e

# Dizin ve değişken tanımlamaları
SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
INSTALL_DIR="$HOME/.local/share/lupus-welcome"
BIN_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"
AUTOSTART_DIR="$HOME/.config/autostart"
COMMAND_NAME="lupus-welcome"
ICON_PATH="$INSTALL_DIR/icons/lupus.png"

# Kaldırma (Uninstall) mod kontrolü
if [ "$1" == "uninstall" ]; then
    echo "=========================================="
    echo "  LupuS Welcome Kaldırılıyor..."
    echo "=========================================="

    echo "[1/4] Uygulama dizini siliniyor -> $INSTALL_DIR"
    rm -rf "$INSTALL_DIR"

    echo "[2/4] Komut siliniyor -> $BIN_DIR/$COMMAND_NAME"
    rm -f "$BIN_DIR/$COMMAND_NAME"

    echo "[3/4] Masaüstü kısayolu siliniyor -> $DESKTOP_DIR/lupus-welcome.desktop"
    rm -f "$DESKTOP_DIR/lupus-welcome.desktop"

    echo "[4/4] Başlangıçta çalıştırma kısayolu siliniyor -> $AUTOSTART_DIR/lupus-welcome.desktop"
    rm -f "$AUTOSTART_DIR/lupus-welcome.desktop"

    # Masaüstü veritabanını güncelle (varsa)
    if command -v update-desktop-database &> /dev/null; then
        update-desktop-database "$DESKTOP_DIR" &> /dev/null || true
    fi

    echo "=========================================="
    echo "  Kaldırma İşlemi Tamamlandı! 🗑️"
    echo "=========================================="
    exit 0
fi

# Kurulum (Install) Modu
echo "=========================================="
echo "  LupuS Welcome Kurulumu Başlatılıyor..."
echo "=========================================="

# Gerekli hedef dizinleri oluştur
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
mkdir -p "$DESKTOP_DIR"

# 1. Uygulama dosyalarını hedef dizine kopyala
echo "[1/3] Uygulama dosyaları kopyalanıyor -> $INSTALL_DIR"
cp -r "$SRC_DIR/welcome.py" "$INSTALL_DIR/"
cp -r "$SRC_DIR/icons" "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/welcome.py"

# 2. Komut (CLI) wrapper betiğini oluştur
echo "[2/3] Komut oluşturuluyor -> $BIN_DIR/$COMMAND_NAME"
cat << 'EOF' > "$BIN_DIR/$COMMAND_NAME"
#!/bin/bash
INSTALL_DIR="$HOME/.local/share/lupus-welcome"
cd "$INSTALL_DIR" || exit 1
exec python3 welcome.py "$@"
EOF
chmod +x "$BIN_DIR/$COMMAND_NAME"

# 3. Masaüstü uygulama (.desktop) kısayolunu oluştur
echo "[3/3] Masaüstü uygulaması (.desktop) oluşturuluyor -> $DESKTOP_DIR/lupus-welcome.desktop"
cat << EOF > "$DESKTOP_DIR/lupus-welcome.desktop"
[Desktop Entry]
Version=1.0
Type=Application
Name=LupuS Welcome
Comment=LupuS Hoş Geldiniz Uygulaması
Exec=$BIN_DIR/$COMMAND_NAME
Icon=$ICON_PATH
Terminal=false
Categories=Utility;System;
StartupNotify=true
EOF
chmod +x "$DESKTOP_DIR/lupus-welcome.desktop"

# Masaüstü veritabanını güncelle (varsa)
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$DESKTOP_DIR" &> /dev/null || true
fi

echo "=========================================="
echo "  Kurulum Başarıyla Tamamlandı! 🎉"
echo "=========================================="
echo "Uygulama Dizini : $INSTALL_DIR"
echo "Komut Adı        : $COMMAND_NAME ($BIN_DIR/$COMMAND_NAME)"
echo "Masaüstü İkonu  : $ICON_PATH"
echo "=========================================="
echo "Terminale '$COMMAND_NAME' yazarak veya uygulama menüsünden başlatabilirsiniz."
echo "Uygulamayı kaldırmak için: ./install.sh uninstall"
