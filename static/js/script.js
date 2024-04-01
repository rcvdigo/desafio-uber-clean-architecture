// Variaveis de controle para avançar e voltar
let currentStep = 1;
const totalSteps = 3;

// Função que avança e faz a troca de campos do formulário

// console.log({'currentStep': currentStep, 'totalSteps': totalSteps});

function nextStep() {
    // console.log({'cli':'cou' , 'currentStep': currentStep, 'totalSteps': totalSteps});
    if (currentStep < totalSteps) {
        if (currentStep === 1) {
            
            // Valida se os campos foram preenchidos
            if (currentStep === 1 && !validateStep(currentStep)) {
                // Se o passo 1 não estiver validado, não avança
                return;
            }

            // Oculta o bloco_um
            document.getElementById('bloco_um').classList.add('hidden');
            // Incrementa o passo atual
            currentStep++;
            // console.log({'esta':'aqui' , 'currentStep': currentStep, 'totalSteps': totalSteps});
            // Mostra o bloco_dois
            document.getElementById('bloco_dois').classList.remove('hidden');
        } else if (currentStep === 2) {
            
            // Valida se os campos foram preenchidos
            if (currentStep === 2 && !validateStep(currentStep)) {
                // Se o passo 1 não estiver validado, não avança
                return;
            }

            // Oculta o bloco_dois
            document.getElementById('bloco_dois').classList.add('hidden');
            // Incrementa o passo atual
            currentStep++;
            // console.log({'entrou':'aqui' , 'currentStep': currentStep, 'totalSteps': totalSteps});
            // Mostra o bloco_tres
            document.getElementById('bloco_tres').classList.remove('hidden');
        } 

        // Atualiza a exibição dos botões de navegação
        if (currentStep === totalSteps) {
            document.querySelector('.btn-primary').style.display = 'none';
            document.querySelector('.btn-secondary').style.display = 'inline-block';
            document.querySelector('#submitBtn').style.display = 'inline-block';
        } else {
            document.querySelector('.btn-primary').style.display = 'inline-block';
            document.querySelector('.btn-secondary').style.display = 'inline-block';
            document.querySelector('#submitBtn').style.display = 'none';
        }
    }
}

// Função que volta e faz a troca de campos do formulário
function prevStep() {
    // console.log(currentStep);
    if (currentStep === 2) {
        // Esconde o bloco_dois
        document.getElementById('bloco_dois').classList.add('hidden');

        // Volta para o bloco_um
        document.getElementById('bloco_um').classList.remove('hidden');

        // Volta o valor da variavel de validação para o valor anterior
        currentStep = 1;
    } else if (currentStep === 3) {
        // console.log(currentStep);
        // Esconde o bloco_dois
        document.getElementById('bloco_tres').classList.add('hidden');

        // Volta para o bloco_um
        document.getElementById('bloco_dois').classList.remove('hidden');
        
        // Volta o valor da variavel de validação para o valor anterior
        currentStep = 2;
    }

    // Atualiza a exibição dos botões de navegação
    if (currentStep === totalSteps) {
        document.querySelector('.btn-primary').style.display = 'none';
        document.querySelector('.btn-secondary').style.display = 'inline-block';
        document.querySelector('#submitBtn').style.display = 'inline-block';
    } else if (currentStep === 1) {
        document.querySelector('.btn-secondary').style.display = 'none';
    } else {
        document.querySelector('.btn-primary').style.display = 'inline-block';
        document.querySelector('.btn-secondary').style.display = 'inline-block';
        document.querySelector('#submitBtn').style.display = 'none';
    }
}

// Validador que verifica se os campos foram preenchidos
function validateStep(currentStep) {
    if (currentStep === 1) {
        const nome = document.getElementById('nome').value.trim();
        const idade = document.getElementById('idade').value.trim();
        const valor = document.getElementById('valor').value.trim();

        if (nome === '' || idade === '' || valor === '') {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return false;
        }

        return true;
    } else if (currentStep === 2) {
        const data = document.getElementById('data').value.trim();
        const chave_pix = document.getElementById('chave-pix').value.trim();
        const telefone = document.getElementById('telefone').value.trim();

        if (data === '' || chave_pix === '' || telefone === '') {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return false;
        }

        return true;
    } 
}

// Função para resetar o formulário
function resetForm() {
    // Limpa todos os campos do formulário
    document.querySelectorAll('input, textarea').forEach(function(element) {
        element.value = '';
    });

    // Volta para o primeiro passo e oculta botão "Voltar" e botão de envio
    currentStep = 1;

    document.querySelector('.btn-back').style.display = 'none';
    document.querySelector('.btn-primary').style.display = 'inline-block';
    document.querySelector('#submitBtn').style.display = 'none';

    // Esconde o bloco_tres
    document.getElementById('bloco_tres').classList.add('hidden');
    // Mostra o bloco_um
    document.getElementById('bloco_um').classList.remove('hidden');
}

// Função que impede a digitação de caracteres no campo valor.
document.getElementById("valor").addEventListener("input", function() {
    // Remove caracteres não numéricos, exceto o ponto
    let cleanedValue = this.value.replace(/[^\d.]/g, '');

    // Verifica se há mais de um ponto na string
    let parts = cleanedValue.split('.');
    if (parts.length > 1) {
        // Se houver, mantém apenas o primeiro ponto e o máximo de dois dígitos após ele
        cleanedValue = parts[0] + '.' + parts.slice(1).join('').substring(0, 2);
    }

    // Atualiza o valor do campo
    this.value = cleanedValue;
});

// Função que impede a digitação de caracteres no campo telefone 
// e faz a formatação de telefone automatica. 
document.getElementById("telefone").addEventListener("input", function() {
    // Remove caracteres não numéricos
    let cleanedValue = this.value.replace(/\D/g, '');

    // Adiciona espaço após os dois primeiros dígitos (DDD)
    if (cleanedValue.length > 2) {
        cleanedValue = cleanedValue.replace(/^(\d{2})(\d)/, '$1 $2');
    }

    // Adiciona hífen após os quatro dígitos seguintes
    if (cleanedValue.length > 7) {
        cleanedValue = cleanedValue.replace(/^(\d{2}) (\d{5})(\d)/, '$1 $2-$3');
    }

    // Limita a quantidade de caracteres após o hífen
    if (cleanedValue.length > 13) {
        cleanedValue = cleanedValue.substring(0, 13);
    }

    // Atualiza o valor do campo
    this.value = cleanedValue;
});

// Inicializa o campo de telefone formatando no padrão universal.
var input = document.querySelector("#telefone");

window.intlTelInput(input, {
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
    initialCountry: "br", // Define o país inicial como Brasil
    separateDialCode: true, // Separa o código do país do número
    nationalMode: false, // Desativa o modo nacional para exibir sempre o código do país
    placeholder: "Digite seu telefone",
    formatOnDisplay: true, // Formata o número enquanto é digitado
    autoPlaceholder: "aggressive", // Adiciona automaticamente o código do país quando o campo está vazio
});

document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    // Captura o valor do número de telefone
    let phone = document.getElementById('telefone').value;

    // Remove os espaços em branco e o caractere "-" do número de telefone
    phone = phone.replace(/\s+/g, '').replace('-', '');

    // Extrai o código do país antes de enviar o formulário
    const div_dial_code = document.querySelector('.iti__selected-flag');
    let codigoPais = div_dial_code.textContent.trim();
    codigoPais = codigoPais.replace('+', '');

    // Captura os valores dos campos do formulário
    const formData = {
        nome: document.getElementById('nome').value,
        idade: parseInt(document.getElementById('idade').value),
        valor: parseFloat(document.getElementById('valor').value.replace(',', '.')), // Converte para float e substitui ',' por '.'
        data: document.getElementById('data').value,
        chavePix: document.getElementById('chave-pix').value,
        telefone: codigoPais + phone,
        assunto: document.getElementById('assunto').value,
        remetente: document.getElementById('remetente').value,
        destinatario: document.getElementById('destinatario').value,
        corpoMensagem: document.getElementById('corpo-mensagem').value
    };

    // Envia os dados para o servidor em formato JSON
    try {
        const response = await fetch('/api/email_sns/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({ "mensagem": formData})
        });

        if (response.ok) {
            // Sucesso
            alert('Dados enviados com sucesso!');
            // Aqui você pode redirecionar para outra página, se necessário
        } else {
            // Erro
            alert('Erro ao enviar os dados. Por favor, tente novamente.');
        }
    } catch (error) {
        // Erro de requisição
        console.error('Erro:', error);
        alert('Ocorreu um erro ao enviar os dados. Por favor, tente novamente.');
    }

    // Após o envio, restaura o estado inicial da página
    resetForm();
});