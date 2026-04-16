import sys
from ultralytics import YOLO
from PIL import Image

def executar_inferencia(caminho_modelo, caminho_imagem):
    print(f"A carregar o modelo: {caminho_modelo}...")
    try:
        model = YOLO(caminho_modelo)
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return

    print(f"A processar a imagem: {caminho_imagem}...")
    # Realiza a predição com um nível de confiança mínimo de 50%
    results = model.predict(source=caminho_imagem, save=True, conf=0.5)

    # Exibe a imagem com as caixas (bounding boxes) desenhadas na tela
    for r in results:
        im_array = r.plot()  # Plota as deteções
        im = Image.fromarray(im_array[..., ::-1])  # Converte as cores de BGR (OpenCV) para RGB (Pillow)
        im.show()
        
    print(f"\nConcluído! A imagem com o resultado foi salva em: {results[0].save_dir}")

if __name__ == "__main__":
    # Verifica se o utilizador passou os argumentos corretos no terminal
    if len(sys.argv) < 3:
        print("Uso correto: python inferencia.py <caminho_do_modelo.pt> <caminho_da_imagem.jpg>")
    else:
        executar_inferencia(sys.argv[1], sys.argv[2])