wheel=$(ls -t ../dist/*.whl | head -n 1)
echo "Installing $wheel..."
python -m pip install "$wheel" --force-reinstall
echo "Done."