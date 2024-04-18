import math
class ShapeError(Exception):
    def __init__(self,message):
        super().__init__(message)
class CoordinateError(Exception):
    def __init__(self,message):
        super().__init__(message)
class Point: #clase punto
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def compute_distance(self,p2):
        distance=((self.x-p2.x)**2 + (self.y-p2.y)**2)**0.5
        return distance
    
class Line: #clase linea compuesta de puntos (punto inicial y final)
    def __init__(self,start_point:Point,end_point:Point,length):
        
        self.length=length#distancia entre ambos puntos => longitud de la arista
        self.start_point=start_point
        self.end_point=end_point


class Shape: #clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        
        self.is_regular=is_regular
        self.vertices=vertices
        self.edges=edges
        self.inner_angles=inner_angles

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar area()") #se usa polimorfismo para definir el metodo area de manera diferente dependiendo de la figura
    
    def compute_perimeter(self):# el perimetro se calcula igual en cualquier caso, por lo que se define inicialmente en la clase shape (la suma de las longitudes se las aristas dentro de la lista "edges")
        perimeter=0
        for edge in self.edges:
            perimeter += edge.length
        return perimeter
            
    
class Rectangle(Shape): #clase rectangulo que hereda de super clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self): 
        width=min(edge.length for edge in self.edges) #la arista con la menor longitud se toma como el ancho del rectangulo
        height=max(edge.length for edge in self.edges) #la arista con la mayor longitud se toma como el alto del rectangulo
        area=width*height
        return area 
    
class Square(Rectangle): #clase cuadrado que hereda de la super clase rectangulo
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):
        
        area=self.edges[0].length**2 #todos sus lados son iguales, por lo que simplemente se toma el primero y se eleva al cuadrado
        return area 

class Triangle(Shape): #clase triangulo que hereda de super clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)
    
    def compute_inner_angles(self): #Se calculan los angulos internos del triangulo a partir de los puntos ingresados utilizando la formula del producto punto de vectores.
        
        angle_list=[]

        vx1=vertices[0].x-vertices[1].x
        vy1=vertices[0].y-vertices[1].y
        vector1=Point(vx1,vy1)
        vx2=vertices[2].x-vertices[1].x
        vy2=vertices[2].y-vertices[1].y
        vector2=Point(vx2,vy2)

        dot_product_1=vx1*vx2+vy1*vy2 
        vector1_lenght=vector1.compute_distance(Point(0,0))
        vector2_lenght=vector2.compute_distance(Point(0,0))

        arcos_1=math.acos(dot_product_1/(vector1_lenght*vector2_lenght))
        angle_1=math.degrees(arcos_1)
        angle_list.append(angle_1)


        vx3=vertices[0].x-vertices[2].x
        vy3=vertices[0].y-vertices[2].y
        vector3=Point(vx3,vy3)
        vx4=vertices[1].x-vertices[2].x
        vy4=vertices[1].y-vertices[2].y
        vector4=Point(vx4,vy4)

        dot_product_2=vx3*vx4+vy3*vy4
        vector3_lenght=vector3.compute_distance(Point(0,0))
        vector4_lenght=vector4.compute_distance(Point(0,0))

        arcos_2=math.acos(dot_product_2/(vector3_lenght*vector4_lenght))
        angle_2=math.degrees(arcos_2)
        angle_list.append(angle_2)

        angle_3=180-angle_2-angle_1
        angle_list.append(angle_3)

        return angle_list
class Isosceles(Triangle): #clase isosceles (dos de tres lados iguales) que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):#se verifica que lado es el que tiene una longitud diferente para tomarlo como la base den triangulo
                           #poder hallar su altura y por tanto su area
        if self.edges[0].length==self.edges[1].length:

            heigth=(self.edges[0].length**2-(self.edges[2].length/2)**2)**0.5
            area=(self.edges[2].length*heigth)/2

            return area


        elif self.edges[0].length==self.edges[2].length:

            heigth=(self.edges[0].length**2-(self.edges[1].length/2)**2)**0.5
            area=(self.edges[1].length*heigth)/2

            return area

        elif self.edges[1].length==self.edges[2].length:

            heigth=(self.edges[1].length**2-(self.edges[0].length/2)**2)**0.5
            area=(self.edges[0].length*heigth)/2

            return area
        
        else: 
            print("El triangulo no es isosceles") #si no tiene dos lados iguales, no es isosceles

class Equilateral(Triangle): #clase equilatero que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self): #todos los lados son iguales, por lo que se toma la longitud de unicamente primero para hallar altura y area del triangulo equilatero

        heigth=(self.edges[0].length**2+(self.edges[0].length/2)**2)**0.5
        area=(self.edges[0].length*heigth)/2

        return area

class TriRectangle(Triangle): #clase triangulo rectangulo que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):
        ordered_edges=sorted(edge.length for edge in self.edges)#se ordena la lista de aristas de menor a mayor longitud

        #la arista con mayor longitud sera la hipotenusa, por lo que para hallar el area solo se toman las dos primeras aristas (las mas pequeñas)
        #como base y altura del rectangulo

        widht=ordered_edges[0]
        height=ordered_edges[1]
        area=(widht*height)/2

        return area
    

class Scalene(Triangle): #clase escaleno que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):

        s=(self.edges[0].length+self.edges[1].length+self.edges[2].length)/2 #semiperimetro= (perimetro/2)
        area=(s*(s-self.edges[0].length)*(s-self.edges[1].length)*(s-self.edges[2].length))**0.5 # formula de Herón , usando el semiperimetro, 
                                                                                                  #para hallar el area del triangulo escaleno sin necesidad de hallar su altura.

        return area
    
if __name__ == "__main__":

    try:
        shape=str(input("¿Que figura desea crear? (Rectangulo/Triangulo): "))
        if shape.lower()=="rectangulo":
            x1=float(input("Ingrese la cordenada en X de la esquina superior izquierdaa:"))
            y1=float(input("Ingrese la cordenada en Y de la esquina superior izquierda:"))
            x2=float(input("Ingrese la cordenada en X de la esquina inferior derecha:"))
            y2=float(input("Ingrese la cordenada en Y de la esquina inferior derecha:"))
            

            if x1==x2 and y1==y2:
                raise CoordinateError (" No se pueden ingresar dos puntos iguales.") #No se puede ingresar un mismo punto, por lo que, en caso de que las x y las y de ambas coordenadas coincidan, 
                                                                                  #se levanta la exepcion CoordinateError que captura errores relacionados con la ubicacion de las coordenadas,
                                                                                  #con el mensaje :" No se pueden ingresar dos puntos iguales.".
            else:
                point_1 = Point(x1,y1)
                point_2 = Point(x2,y1)
                point_3 = Point(x2,y2)
                point_4 = Point(x1,y2)

                edges = [
                Line(point_1, point_2, point_1.compute_distance(point_2)),
                Line(point_2, point_3,point_2.compute_distance(point_3)), 
                Line(point_3, point_4,point_3.compute_distance(point_4)),
                Line(point_4, point_1,point_4.compute_distance(point_1))]
                vertices = [point_1, point_2, point_3,point_4] 

                if abs(x1-x2)==abs(y1-y2):
                    square_1=Square(vertices, edges, [90,90,90,90])
                    print(f"Área del cuadrado: {square_1.compute_area()},Perimetro del cuadrado: {square_1.compute_perimeter()}, Suma de ángulos internos del cuadrado: {square_1.compute_inner_angles()}") 
                else:
                    rectangle_1=Rectangle(vertices, edges, [90,90,90,90])
                    print(f"Área del rectangulo: {rectangle_1.compute_area()},Perimetro del rectangulo: {rectangle_1.compute_perimeter()}, Suma de ángulos internos del rectangulo: {rectangle_1.compute_inner_angles()}") 
    
        elif shape.lower()=="triangulo":
            x1=float(input("Ingrese la cordenada en X del primer punto:"))
            y1=float(input("Ingrese la cordenada en Y del primer punto:"))
            x2=float(input("Ingrese la cordenada en X del segundo punto:"))
            y2=float(input("Ingrese la cordenada en Y del segundo punto:"))
            x3=float(input("Ingrese la cordenada en X del tercer punto:"))
            y3=float(input("Ingrese la cordenada en Y del tercer punto:"))

            if (x1==x2 and y1==y2) or (x1==x3 and y1==y3) or (x2==x3 and y2==y3):
                raise CoordinateError (" No se puede ingresar un punto más de una vez.") # De los tres puntos ingresados, es suficiente que dos de ellos coincidan 
                                                                                         #para que se levante la exepción CoordinateError con el mensaje:" No se puede ingresar 
                                                                                         #un punto más de una vez.".
            point_1 = Point(x1,y1)
            point_2 = Point(x2,y2)
            point_3 = Point(x3,y3)


            edges = [
            Line(point_1, point_2, point_1.compute_distance(point_2)),
            Line(point_2, point_3,point_2.compute_distance(point_3)), 
            Line(point_3, point_1,point_3.compute_distance(point_1))]
            vertices = [point_1, point_2, point_3] 

            if point_1.compute_distance(point_2) != point_2.compute_distance(point_3) and point_1.compute_distance(point_2) != point_3.compute_distance(point_1) and point_2.compute_distance(point_3) != point_3.compute_distance(point_1):
                triangle_1=Scalene(vertices, edges, [50,65,65])
                if triangle_1.compute_area()==0: #Si el area del triangulo es 0, significa que los puntos no corresponden a un triangulo, si no, a una linea. 
                                                 #Esto significa que los puntos son colineales (la pendiente entre cada uno de ellos es igual).
                    raise CoordinateError ("Los puntos inglesados son colineales. No se puede crear un triangulo.")
                    #En caso de que se confirme que se trata de una linea, se levanta la exepcion CoordinateError con el mensaje:"Los puntos ingresados son colineales. No se puede crear un triangulo.".
                else:
                    print(f"Área del triangulo escaleno: {triangle_1.compute_area()},Perimetro del triangulo escaleno: {triangle_1.compute_perimeter()}, Ángulos internos del triangulo escaleno: {triangle_1.compute_inner_angles()}, ") 
            if (point_1.compute_distance(point_2)==point_2.compute_distance(point_3) and point_1.compute_distance(point_2) !=point_3.compute_distance(point_1)) or (point_1.compute_distance(point_2)==point_3.compute_distance(point_1) and point_1.compute_distance(point_2) !=point_2.compute_distance(point_3)) or (point_2.compute_distance(point_3)==point_3.compute_distance(point_1) and point_2.compute_distance(point_3) !=point_1.compute_distance(point_2)):
                triangle_1=Isosceles(vertices, edges, [50,65,65])
                if triangle_1.compute_area()==0:
                    raise CoordinateError ("Los puntos inglesados son colineales. No se puede crear un triangulo.")
                else:
                    print(f"Área del triangulo isoceles: {triangle_1.compute_area()},Perimetro del triangulo isoceles: {triangle_1.compute_perimeter()}, Ángulos internos del triangulo isoceles: {triangle_1.compute_inner_angles()}") 
            if point_1.compute_distance(point_2)==point_2.compute_distance(point_3)==point_3.compute_distance(point_1):
                triangle_1=Equilateral(vertices, edges, [50,65,65])
                #Triangulo equilatero no implementa CoordinateError para verificar que no se trarte de puntos colineales, 
                #ya que implementa CoordinateError para que ningun punto se repita, lo que significa que si los puntos ingresados son colineales, 
                #no hay posibilidad de que la longitud entre los tres puntos sea igual ("Triangulo Equilatero").

                print(f"Área del triangulo equilatero: {triangle_1.compute_area()},Perimetro del triangulo equilatero: {triangle_1.compute_perimeter()}, Ángulos internos del triangulo equilatero: {triangle_1.compute_inner_angles()}")
            if  (point_1.compute_distance(point_2)== (point_2.compute_distance(point_3)**2+point_3.compute_distance(point_1)**2)**0.5) or (point_2.compute_distance(point_3)== (point_3.compute_distance(point_1)**2+point_1.compute_distance(point_2)**2)**0.5) or (point_3.compute_distance(point_1)== (point_1.compute_distance(point_2)**2+point_2.compute_distance(point_3)**2)**0.5):
                triangle_1=TriRectangle(vertices, edges, [50,65,65])
                if triangle_1.compute_area()==0:
                    raise CoordinateError ("Los puntos inglesados son colineales. No se puede crear un triangulo.")
                else:
                    print(f"Área del triangulo rectangulo: {triangle_1.compute_area()},Perimetro del triangulo rectangulo: {triangle_1.compute_perimeter()}, Ángulos internos del triangulo rectangulo: {triangle_1.compute_inner_angles()}")
        
        else:
            raise ShapeError ("Figura no disponible")
            
    except CoordinateError as e:
        print(f"Error: {e}")
    except ShapeError as e:
        print(f"Error: {e}")
    except ValueError:
        print(f"Error: No se aceptan valores no numericos.") # En el imput se aseguro que se aceptaran numeros tanto enteros como decimales, 
                                                              #por lo que ValueError se levanta solo en caso de que se ingrese un valor no numerico, 
                                                              #como una letra o un signo.


