programa
{
	
	funcao inicio()
	{
		const inteiro maior = 18
		inteiro idade, anos

		escreva ("\nDigite sua idade: ")
		leia(idade)

		se (idade >= maior)
			escreva ("Voce e maior de idade")
		senao
		{
			anos = maior - idade
			escreva ("Faltam " ,anos, " para atigir a maioridade")
		}
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 32; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */