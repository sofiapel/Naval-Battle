#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

int casos = 1;



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
	while(puedoLeer(fp)){
		int b = sacarInfo(fp);
		laburar(b);
	}

	return 0;
}

int puedoLeer(){
	--casos;
	return casos >= 0;
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

void laburar(int b){
	for(int i=0; i < b; i++){
		if (barcos[i].orientacion == 'h')
			for(int k=0; k < barcos[i].longitud; k++)
				printf("(%c,%d)", barcos[i].posicion.letra , (barcos[i].posicion.num) + k);
		else
			for(int k=0; k<barcos[i].longitud; k++)
				printf("(%c,%d)", (barcos[i].posicion.letra)+k , barcos[i].posicion.num);
			
				
		
		
		}
	
		
			 
}


// 4 v A 1    
// 5 h C 3    
// 6 v B 2    
