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
	int orientacion; //1 vertical 0 horizontal
	Pos posicion;
} Barco;

int flota(FILE * fp, int n);
int puedoLeer();
void sacarInfo();
void laburar();


int main(){
	FILE * fp;
	fp = fopen("configuraciones.txt", "r");
	while(puedoLeer()){
		sacarInfo();
		laburar();
	}
	// flota(fp, n);

	return 0;
}


 int flota(FILE * fp, int n){
	size_t size = 50;
	char * buff;
	char * pch;
	int cnt = 0;
	int x;
	buff = (char*) malloc (size * sizeof(char));
	
	int linesRead = 0;
	while(linesRead < 6*n - 4){
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

int puedoLeer(){
	return 0;
}

void sacarInfo(){

}

void laburar(){

}