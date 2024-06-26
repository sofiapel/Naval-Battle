#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

typedef struct{
	char letra;
	int  num;
} Pos;

typedef struct {
	int longitud;
	char orientacion;
	Pos posicion;
} Barco;

Barco barcos[100];

int flota(FILE * fp, int n);
int puedoLeer();
int sacarInfo();
void laburar();


int main(){
	FILE * fp;
	fp = fopen("configuraciones.txt", "r");
	int caso, b;
	printf("Ingrese el número del caso porfi: ");
	scanf("%d", &caso);
	for (int i = 0; i < caso; i++)
		b = sacarInfo(fp);
	laburar(b);

	return 0;
}

int sacarInfo(FILE * fp){
	char c,g[100],letra;
	int l, n, b, num;

	fscanf(fp,"(%d)\n", &n);
	fscanf(fp,"Barcos : %d\n", &b);
	fscanf(fp,"Longitudes");
	for(int i = 0; i < b; i++ ){
		fscanf(fp," %c %d",&c,&l);
		barcos[i].longitud = l;
	}
	fscanf(fp,"\n");
	fscanf(fp,"Orientaciones");
	for(int i= 0; i<b;i++){
		fscanf(fp," %c %s",&c, g);
		barcos[i].orientacion = g[0];
	}
	fscanf(fp,"\n");
	fscanf(fp,"Posiciones iniciales");
	for(int i=0; i< b; i++){
		fscanf(fp," %c (%c,%d)", &c,&letra,&num);
		barcos[i].posicion.letra = letra;
		barcos[i].posicion.num = num;
	}
	fscanf(fp,"\n\n");
	return b;
}

void laburar(int b ){
	FILE * fp;
	fp =fopen("Salida.txt","w");
	for(int i=0; i < b; i++){
		fprintf(fp,"[");
		if (barcos[i].orientacion == 'h'){
			for(int k=0; k < barcos[i].longitud; k++){
				if(k>0) fprintf(fp,",");
				fprintf(fp,"(%c,%d)", barcos[i].posicion.letra ,barcos[i].posicion.num +  k);
			}
		}
		else {
			for(int k=0; k<barcos[i].longitud; k++){
			    if(k>0) fprintf(fp,",");
				fprintf(fp,"(%c,%d)", (barcos[i].posicion.letra)+k , barcos[i].posicion.num);
			}
		}
		fprintf(fp,"]\n");
	}
}


// 4 v A 1    
// 5 h C 3    
// 6 v B 2    
