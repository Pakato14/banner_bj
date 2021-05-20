from PIL import Image
#pega as imagens que irá mesclar
testBanner = Image.open('modelo padrão dos banners.jpg')
juntaImg = Image.open('img_peca/131579PK.png')
veiculoImg = Image.open('img_veiculo/Audi Sedan.png')

#junta as imagens
testBanner.paste(juntaImg.rotate(45), (200, 800), mask=juntaImg)
testBanner.save('TESTE_IMG/teste.png')
