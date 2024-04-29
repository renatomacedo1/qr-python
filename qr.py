import cv2
from pyzbar.pyzbar import decode

def ler_qr_code():
    # Inicializa a captura de vídeo da webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Captura um quadro da webcam
        ret, frame = cap.read()
        
        # Decodifica os códigos QR presentes no quadro
        codigos = decode(frame)
        
        # Exibe o quadro na janela
        cv2.imshow('Leitor de QR Code', frame)
        
        # Verifica se um código QR foi detectado
        if codigos:
            # Itera sobre os códigos QR encontrados
            for codigo in codigos:
                # Extrai o conteúdo do código QR
                conteudo = codigo.data.decode('utf-8')
                print("Conteúdo do QR Code:", conteudo)
                
            # Aguarda 2 segundos antes de fechar a janela
            cv2.waitKey(2000)
            break
        
        # Verifica se a tecla 'q' foi pressionada para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera a captura de vídeo e fecha a janela
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ler_qr_code()
