programa
{
	funcao inicio()
	{	
		cadeia nome, fim
		caracter sexo, genero
		inteiro quantEntrev = 0, homemJovem = 0, homemAdulto = 0, homemExpert = 0,
		mulherJovem = 0, mulherAdulto = 0, mulherExpert = 0
		real peso, altura, imc, idade,
		mediaIdadeHomemJovem =0, mediaIdadeHomemAdulto = 0, mediaIdadeHomemExpert = 0, 
		mediaIdadeMulherJovem = 0, mediaIdadeMulherAdulto = 0, mediaIdadeMulherExpert = 0,
		mediaPesoHomemJovem = 0, mediaPesoHomemAdulto = 0, mediaPesoHomemExpert = 0,
		mediaPesoMulherJovem = 0, mediaPesoMulherAdulto = 0, mediaPesoMulherExpert = 0,
		mediaAlturaHomemJovem = 0, mediaAlturaHomemAdulto = 0, mediaAlturaHomemExpert = 0,
		mediaAlturaMulherJovem = 0, mediaAlturaMulherAdulto = 0, mediaAlturaMulherExpert = 0,
		somaIdadeHomemJovem = 0 , somaIdadeHomemAdulto = 0, somaIdadeHomemExpert = 0, 
		somaIdadeMulherJovem = 0, somaIdadeMulherAdulto = 0, somaIdadeMulherExpert = 0,
		somaPesoHomemJovem = 0, somaPesoHomemAdulto = 0, somaPesoHomemExpert = 0, 
		somaPesoMulherJovem = 0, somaPesoMulherAdulto = 0, somaPesoMulherExpert = 0, 
		somaAlturaHomemJovem = 0, somaAlturaHomemAdulto = 0, somaAlturaHomemExpert = 0,
		somaAlturaMulherJovem = 0, somaAlturaMulherAdulto = 0, somaAlturaMulherExpert = 0

		
		faca
		 {		
		faca
		{
			escreva("\nDigite sua idade: " )
			leia(idade)
			
			se (idade <18)
			{
				limpa()
				escreva ("\nVoce precisa ter mais de 18 anos para preencher a pesquisa")
			}
		}
		enquanto (idade<18)
				
			escreva("\nDigite seu nome: " )
			leia(nome)
			escreva("\nDigite 1 para homem e 2 para mulher: " )
			leia(genero)
			escreva("\nDigite seu peso: " )
			leia(peso)
			escreva("\nDigite sua altura: " )
			leia(altura)

		imc = (peso / (altura * altura)) * 10000
		escreva (imc)

			
			se (imc>=18.5 e imc<=24.9)
				 escreva("\nParabens seu peso esta ok")
			senao se (imc>=25)
				 escreva("\nVoce está acima do peso")
			senao se (imc>=18.4)
				 escreva("\nVoce está abaixo do peso")
				 
			se (idade >= 18 e idade < 32) {
		    escreva("\nJovem\n")			
	        }
	        senao se (idade >= 32 e idade < 61) {
		    escreva("\nAdulto\n")
		    }
	        senao se (idade >= 62) {
		    escreva("\nExpert\n")
	        }
			se (idade >= 18 e idade <=32 e genero == '1'){
			escreva("\nHomens Jovens\n")
			quantEntrev = quantEntrev + 1
			somaIdadeHomemJovem = (somaIdadeHomemJovem + idade)
			somaPesoHomemJovem = (somaPesoHomemJovem + peso)
			somaAlturaHomemJovem = (somaAlturaHomemJovem + altura)
			homemJovem = homemJovem + 1			
			
		}

		se (idade >= 18 e idade <=32 e genero == '2'){
			escreva("\nMulheres Jovens\n")
			quantEntrev = quantEntrev + 1
			somaIdadeMulherJovem = (somaIdadeMulherJovem + idade)
			somaPesoMulherJovem = (somaPesoMulherJovem + peso)
			somaAlturaMulherJovem = (somaAlturaMulherJovem + altura)
			mulherJovem = mulherJovem + 1
						
		}
		se (idade >= 33 e idade <= 61 e genero == '1'){
			escreva("\nHomens Adultos\n")
			quantEntrev = quantEntrev + 1 
			somaIdadeHomemAdulto = (somaIdadeHomemAdulto + idade)
			somaPesoHomemAdulto = (somaPesoHomemAdulto + peso)
			somaAlturaHomemAdulto = (somaAlturaHomemAdulto + altura)
			homemAdulto = homemAdulto + 1
			
		}

		se (idade >= 33 e idade <= 61 e genero == '2'){
			escreva("\nMulheres Adultas\n")
			quantEntrev = quantEntrev + 1 
			somaIdadeMulherAdulto = (somaIdadeMulherAdulto + idade)
			somaPesoMulherAdulto = (somaPesoMulherAdulto + peso)
			somaAlturaMulherAdulto = (somaAlturaMulherAdulto + altura)
			mulherAdulto = mulherAdulto + 1
			
		}
		
		se (idade > 61 e genero == '1'){
			escreva("\nHomens Experts\n")
			quantEntrev = quantEntrev + 1
			somaIdadeHomemExpert = (somaIdadeHomemExpert + idade)
			somaPesoHomemExpert = (somaPesoHomemExpert + peso)
			somaAlturaHomemExpert = (somaAlturaHomemExpert + altura)
			homemExpert = homemExpert +1
			
		}

		se (idade > 61 e genero == '2'){
			escreva("\nMulheres Experts\n")
			quantEntrev = quantEntrev + 1
			somaIdadeMulherExpert = (somaIdadeMulherExpert + idade)
			somaPesoMulherExpert = (somaPesoMulherExpert + peso)
			somaAlturaMulherExpert = (somaAlturaMulherExpert + altura)
			mulherExpert = mulherExpert +1
			
		}

			escreva ("\nDeseja continuar a pesquisa? Digite 1 para sim e 2 para nao: ")
			leia(fim)
		    }
		    enquanto (fim != "2")
						
			mediaIdadeHomemJovem = (somaIdadeHomemJovem / homemJovem)
			mediaIdadeMulherJovem = (somaIdadeMulherJovem / mulherJovem)
			mediaIdadeHomemAdulto = (somaIdadeHomemAdulto / homemAdulto)
			mediaIdadeMulherAdulto = (somaIdadeMulherAdulto / mulherAdulto)
			mediaIdadeHomemExpert = (somaIdadeHomemExpert / homemExpert)
			mediaIdadeMulherExpert = (somaIdadeMulherExpert / mulherExpert)
			mediaPesoHomemJovem = (somaPesoHomemJovem / homemJovem)
			mediaPesoMulherJovem = (somaPesoMulherJovem / mulherJovem)
			mediaPesoHomemAdulto = (somaPesoHomemAdulto / homemAdulto)
			mediaPesoMulherAdulto = (somaPesoMulherAdulto / mulherAdulto)
			mediaPesoHomemExpert = (somaPesoHomemExpert / homemExpert)
			mediaPesoMulherExpert = (somaPesoMulherExpert / mulherExpert)
			mediaAlturaHomemJovem = (somaAlturaHomemJovem / homemJovem)
			mediaAlturaMulherJovem = (somaAlturaMulherJovem / mulherJovem)
			mediaAlturaHomemAdulto = (somaAlturaHomemAdulto / homemAdulto)
			mediaAlturaMulherAdulto = (somaAlturaMulherAdulto / mulherAdulto)
			mediaAlturaHomemExpert = (somaAlturaHomemExpert / homemExpert)
			mediaAlturaMulherExpert = (somaAlturaMulherExpert / mulherExpert)
					
			
			escreva("\nQuantidade de entrevistados: ", quantEntrev)
				
			se (homemJovem > 0){
				escreva("\nHomens Jovens\n")
				escreva(homemJovem ," Participantes\n")
				escreva("\nIdade: ",mediaIdadeHomemJovem)
				escreva("\nPeso: ",mediaPesoHomemJovem)
				escreva("\nAltura: ",mediaAlturaHomemJovem)
				
			}
			se (mulherJovem > 0){
				escreva("\nMulheres Jovens\n")
				escreva(mulherJovem ," Participantes\n")
				escreva("\nIdade: ",mediaIdadeMulherJovem)
				escreva("\nPeso: ",mediaPesoMulherJovem)
				escreva("\nAltura: ",mediaAlturaMulherJovem)
				
			}
			se(homemAdulto > 0){
				escreva("\nHomens Adultos\n")
				escreva(homemAdulto ," Participantes\n")
				escreva("\nIdade: ",mediaIdadeHomemAdulto)
				escreva("\nPeso: ",mediaPesoHomemAdulto)
				escreva("\nAltura: ",mediaAlturaHomemAdulto)
				
			}
			
			se (mulherAdulto > 0){
				escreva("Mulheres Adultas!\n")
				escreva(mulherAdulto ," Participantes\n")
				escreva("\nIdade: ",mediaIdadeMulherAdulto)
				escreva("\nPeso: ",mediaPesoMulherAdulto)
				escreva("\nAltura: ",mediaAlturaMulherAdulto)
				
			}
			se(homemExpert > 0){
				escreva("Homens Experts!\n")
				escreva(homemExpert ," Participantes\n")
				escreva("\nIdade: ",mediaIdadeHomemExpert)
				escreva("\nPeso: ",mediaPesoHomemExpert)
				escreva("\nAltura: ",mediaAlturaHomemExpert)
				
			}
			se(mulherExpert > 0){
				escreva("Mulheres Experts!\n")
				escreva(mulherExpert ," Participantes\n")
				escreva("\nIdade: ",mediaIdadeMulherExpert)
				escreva("\nPeso: ",mediaPesoMulherExpert)
				escreva("\nAltura: ",mediaAlturaMulherExpert)
				
			}

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2168; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */