from Shape_Package.classShape import *

def main():
    point_1 = Point(2,1)
    point_2 = Point(6,1)
    point_3 = Point(4,6)
    edges = [
        Line(point_1, point_2, point_1.compute_distance(point_2)),
        Line(point_1, point_3,point_1.compute_distance(point_3)), 
        Line(point_2, point_3,point_2.compute_distance(point_3))]
    vertices = [point_1, point_2, point_3] 
    triangle_1 = Isosceles(vertices, edges, [50,65,65]) #Se crea un triangulo isosceles
    print(f"Área: {triangle_1.compute_area()},Perimetro: {triangle_1.compute_perimeter()}, Suma de ángulos internos: {triangle_1.compute_inner_angles()}") 

if __name__ == "__main__":
    main()
