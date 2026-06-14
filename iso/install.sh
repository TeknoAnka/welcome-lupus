#!/bin/bash

# Proje dizinini al
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
BIN_DIR="$HOME/.local/bin"
COMMAND_NAME="lupus-welcome"
WRAPPER_PATH="$BIN_DIR/$COMMAND_NAME"

# .local/bin dizini yoksa oluştur
mkdir -p "$BIN_DIR"

echo "Kurulum başlatılıyor..."

# Çalıştırıcı (wrapper) betiği oluştur
cat << EOF > "$WRAPPER_PATH"
#!/bin/bash
cd "$PROJECT_DIR"
python3 welcome.py "\$@"
EOF

# İzinleri ayarla
chmod +x "$WRAPPER_PATH"
chmod +x "$PROJECT_DIR/welcome.py"

echo "--------------------------------------------------"
echo "Kurulum tamamlandı!"
echo "Artık terminale '$COMMAND_NAME' yazarak uygulamayı başlatabilirsiniz."
echo "Not: Eğer komut hemen çalışmazsa terminali kapatıp açın veya 'source ~/.bashrc' (veya kullandığınız kabuk ayar dosyasını) çalıştırın."
echo "--------------------------------------------------"
