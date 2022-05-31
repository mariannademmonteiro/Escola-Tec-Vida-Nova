programa
{
	funcao inicio()
	{
		inteiro candidato_a = 0, candidato_b = 0, voto = 0
		
		inteiro brancos = 0, nulos = 0, total_votos = 0
		
		real porcentagem_candidato_a, porcentagem_candidato_b
		
		real porcentagem_brancos, porcentagem_nulos
		
		inteiro total_de_votos
		
		faca
		{
			limpa()
			escreva("\nEscolha seu candidato ou tecle zero para encerrar\n\n")
			
			escreva("  1 -> Candidato A\n")
			escreva("  2 -> Candidato B\n")
			escreva("  3 -> Branco\n")
			
			escreva("\nQualquer número diferente de 0, 1, 2 e 3 anulará o seu voto\n")
			escreva("Digite seu voto: ")
			
			leia(voto)
			limpa()

		escolha (voto)
			{
				caso 0:
				    escreva ("Votação encerrada!\n")
				    total_de_votos = candidato_a + candidato_b + brancos + nulos
				    porcentagem_candidato_a =(100 * candidato_a) / total_de_votos
				    porcentagem_candidato_b =(100 * candidato_b) / total_de_votos
				    porcentagem_brancos =(100 * brancos) / total_de_votos
				    porcentagem_nulos =(100 * nulos) / total_de_votos
				    escreva("\nporcentagem candidato_a: ", porcentagem_candidato_a, "%")
				    escreva("\nporcentagem candidato_b: ", porcentagem_candidato_b, "%")
				    escreva("\nporcentagem brancos: ", porcentagem_brancos, "%")
				    escreva("\nporcentagem nulos: ", porcentagem_nulos, "%")
				    escreva("\ntotal de votos: ", total_de_votos)
				    se (candidato_a > candidato_b)
				    escreva("\ncandidato_a ganhou a eleiçao")
				    se (candidato_b > candidato_a)
				    escreva("\ncandidato_b ganhou a eleiçao")
				    se (candidato_a == candidato_b)
				    escreva("\nninguem ganhou")
				pare
				
				
				caso 1: 
			 		candidato_a = candidato_a + 1 // Soma um voto para o candidato A
			 	pare
			 	
			 	caso 2: 
			 		candidato_b = candidato_b + 1  //Soma um voto para o candidado B
			 	pare
			 	
			 	caso 3: 
			 		brancos = brancos + 1 // Soma um voto em branco
			 	pare
			 	
			 	caso contrario:
			 		nulos = nulos + 1 // Opção inválida. Soma um voto nulo
			}			 
		}
		enquanto(voto != 0)
		
		
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2048; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */