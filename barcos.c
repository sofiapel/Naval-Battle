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
	int orientacion; //1 vertical 0 horizontal
	Pos posicion;
} Barco;

int flota(FILE * fp, int n);
int puedoLeer();
int sacarInfo();
void laburar();


int main(){
	FILE * fp;
	fp = fopen("configuraciones.txt", "r");
	while(puedoLeer(fp)){
		sacarInfo();
		laburar();
	}

	return 0;
}

int puedoLeer(){
	--casos;
	return casos >= 0;
}

int sacarInfo(FILE * fp){
	int n;
	int b;
	fscanf(fp,"(%d)\n", &n);
	fscanf(fp,"Barcos : %d\n", &b);
	printf("%d", b);
	return b;


	size_t size = 50;
	char * buff;
	char * pch;
	int cnt = 0;
	int x;
	buff = (char*) malloc (size * sizeof(char));
	
	int linesRead = 0;
	while(linesRead < 2){
		getline(&buff, &size,fp);
		linesRead++;
	}

	pch = strtok (buff,":\n");
	
	while (pch != NULL){
		cnt++;
		if(cnt == 2) x = atoi(pch);
		pch = strtok (NULL,":\n");
	}

	printf("%d\n",x);
	return x; 
}

void laburar(){
	printf("laburar\n");

}