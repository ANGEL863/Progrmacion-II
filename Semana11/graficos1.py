import matplotlib.pyplot as plt

Res = ["Taco bell","Pizza Hut","Wendys","McDonalds","China Work"]
frec= [1,15,3,11,2]
colores = ["purple","blue","yellow","black","green"]
plt.bar(Res,frec,color=colores)
plt.title("comidas")
plt.xlabel("Restaurantes")
plt.ylabel("Frecuencia")
plt.show()