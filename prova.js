// 1) Variáveis e Apresentação
let nome = "Guilherme Luiz";
let minhaAltura = 1.80; // Usei a variável que você criou
let serie = "3º ano";
let turma = "DSC";

console.log(`Olá, meu nome é ${nome}, minha altura é ${minhaAltura}, sou da série ${serie} e turma ${turma}.`);

// 2) Lista com 3 esportes (Simplificado para facilitar a busca depois)
const esportes = ["Beisebol", "Hockey", "Basquete"];

// 3) Condição de altura
const alturaProf = 1.73;
if (minhaAltura > alturaProf) {
    console.log("Você é maior que o professor Patrick.");
} else {
    console.log("Você é menor ou tem a mesma altura que o professor Patrick.");
}

// 4) Função que mostra os esportes com laço de repetição
function mostrarEsportes(lista) {
    for (let i = 0; i < lista.length; i++) {
        console.log(`Esporte: ${lista[i]}`);
    }
}
mostrarEsportes(esportes);

// 5) Verifica se "natação" existe na lista
if (esportes.includes("natação")) {
    console.log("O esporte natação existe na lista.");
} else {
    console.log("O esporte natação não está na lista.");
}

// 6) Laço de repetição que conta de 0 até -10
for (let contador = 0; contador >= -10; contador--) {
    console.log(contador);
}
