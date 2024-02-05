function jogoPedraPapelTesoura(jogadaPessoa) {
    const jogadasPossiveis = ['pedra', 'papel', 'tesoura'];


    const indiceMaquina = Math.floor(Math.random() * 3);
    const jogadaMaquina = jogadasPossiveis[indiceMaquina];
    console.log('Jogada da Máquina:', jogadaMaquina);

    if (
        (jogadaPessoa === 'pedra' && jogadaMaquina === 'tesoura') 
        (jogadaPessoa === 'tesoura' && jogadaMaquina === 'papel') 
        (jogadaPessoa === 'papel' && jogadaMaquina === 'pedra')
    ) {
        return 'Jogador';
    } else if (
        (jogadaMaquina === 'pedra' && jogadaPessoa === 'tesoura') 
        (jogadaMaquina === 'tesoura' && jogadaPessoa === 'papel') 
        (jogadaMaquina === 'papel' && jogadaPessoa === 'pedra')
    ) {
        return 'Máquina';
    } else {
        return 'Empate';
    }
}

const jogadaPessoa = "pedra";
const resultado = jogoPedraPapelTesoura(jogadaPessoa);
console.log(resultado);

const jogada1 = "pedra"
const jogada2 = "pedra"


// pedra tesoura
// tesoura corta papel
// papel enrola pedra
if (jogada1 === 'pedra' && jogada2 === "tesoura"  jogada1 === 'tesoura' && jogada2 === 'papel'  jogada1 === 'papel' && jogador2 === 'pedra') {
    console.log('jogador1');
} else if (jogada2 === 'pedra' && jogada1 === "tesoura"  jogada2 === 'tesoura' && jogada1 === 'papel'  jogada2 === 'papel' && jogada1 === 'pedra') {
    console.log('jogador2');
} else {
    console.log('empate');
}