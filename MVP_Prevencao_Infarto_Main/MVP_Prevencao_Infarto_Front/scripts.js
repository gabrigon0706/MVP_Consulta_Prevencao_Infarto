const maxItems = 16; // Número máximo de itens no formulário
let currentItem = 1; // Item atual, começa com 1

// Adiciona um ouvinte de eventos para a tecla Enter em todos os campos de entrada
document.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        nextItem();
    }
});

// Obtém o elemento do próximo item e o exibe
function nextItem() {

    // Verifica se o item atual está validado
    if (!validateCurrentItem()) {
        alert("Preencha todos os campos antes de avançar.");
        return false;
    }
    // Esconde o elemento do item atual
    const currentItemElement = document.getElementById(`item${currentItem}`);
    if (currentItemElement) {
        currentItemElement.style.display = "none";
        currentItem++;

        // Exibe o próximo elemento se não atingiu o máximo de itens
        if (currentItem <= maxItems) {
            const nextItemElement = document.getElementById(`item${currentItem}`);
            if (nextItemElement) {
                nextItemElement.style.display = "block";

                // Exibe o botão "Voltar" se não estiver no primeiro item
                if (currentItem > 1) {
                    document.getElementById("backButton").style.display = "block";
                }
            }
        } else {

            // Exibe o botão "Gerar Predição" no último item
            console.error(`Número máximo de itens atingido.`);
            document.getElementById("nextButton").style.display = "none";
            document.getElementById("backButton").style.display = "none";
            document.getElementById("predictionButton").style.display = "block";
            generateTable();
            return false;
        }
    } else {
        console.error(`Elemento item${currentItem} não encontrado.`);
    }
    console.log("Current Item:", currentItem);
    return true;
}

    // Gera a tabela ao pressionar o botão "Avançar" no último item
function generateTable() {
    displayResults();
}

// Função para validar todos os itens
function validateAllItems() {
    for (let i = 1; i <= maxItems; i++) {
        const currentFields = document.querySelectorAll(`#item${i} input, #item${i} select`);
        for (const field of currentFields) {
            if (field.type === 'number' && isNaN(field.valueAsNumber)) {
                return false;
            } else if (field.value.trim() === '') {
                return false;
            }
        }
    }
    return true;
}

// Função para retroceder para o item anterior no formulário. Oculta o item atual e decrementa o índice do item atual
function prevItem() {
    const currentItemElement = document.getElementById(`item${currentItem}`);
    if (currentItemElement) {
        currentItemElement.style.display = "none";
        currentItem--;

        // Obtém o elemento do item anterior e exibe
        const prevItemElement = document.getElementById(`item${currentItem}`);
        if (prevItemElement) {
            prevItemElement.style.display = "block";

            // Exibe o botão "Avançar" se não estiver no último item
            if (currentItem < maxItems) {
                document.getElementById("nextButton").style.display = "block";
            }
        } else {
            document.getElementById("backButton").style.display = "none";
        }
    } else {
        console.error(`Elemento item${currentItem} não encontrado.`);
    }

    console.log("Current Item:", currentItem);

      // Verifica se o botão "Voltar" deve ser oculto
      const backButton = document.getElementById("backButton");
      if (backButton && currentItem <= 1) {
          backButton.style.display = "none";
      }
}

//Valida os campos do item atual, garantindo que os valores numéricos sejam válidos
function validateCurrentItem() {
    const currentFields = document.querySelectorAll(`#item${currentItem} input, #item${currentItem} select`);

    for (const field of currentFields) {
        if (field.type === 'number') {
            const numericValue = parseFloat(field.value);
            if (isNaN(numericValue)) {
                return false;
            }
            const min = parseFloat(field.getAttribute('min'));
            const max = parseFloat(field.getAttribute('max'));  
            if (numericValue < min || numericValue > max) {
                alert(`O valor para ${field.placeholder} deve estar entre ${min} e ${max}.`);
                return false;
            }
        } else if (field.value.trim() === '') {
            return false;
        }
    }
    return true;
}

//Submete o formulário, validando o item atual, avançando para o próximo item e exibindo os resultados
function submitForm() {
    if (!validateCurrentItem()) {
        alert("Preencha todos os campos antes de avançar.");
        return;
    }
    if (!nextItem()) {
        return;
    }
    displayResults();
}

// Obtém a referência para a tabela
function displayResults() {
    const table = document.getElementById("resultTable");

    if (!table) {
        console.error("Tabela não encontrada.");
        return;
    }
    const tbody = table.getElementsByTagName("tbody")[0];

    if (!tbody) {
        console.error("Corpo da tabela não encontrado.");
        return;
    }

    const headerExists = tbody.rows.length > 0;
    
    const rowData = [];

    for (let i = 1; i <= maxItems; i++) {
        const valueElement = document.getElementById(`newItem${i}`);

        if (valueElement) {
            let value;

            if (valueElement.tagName === 'SELECT') {
                const selectedOption = valueElement.options[valueElement.selectedIndex];
                value = selectedOption ? selectedOption.value : undefined;
            } else {
                value = valueElement.value;
            }

            if (value === undefined) {
                console.error(`Valor indefinido para newItem${i}.`);
                console.error('valueElement:', valueElement);
                return;
            }

            rowData.push(value.trim());
        } else {
            console.error(`Elemento newItem${i} não encontrado ou é nulo.`);
            return;
        }
    }

    // Exiba os dados de depuração no console
    console.log('Row Data:', rowData);

    // Adiciona uma nova linha com os dados
    const row = tbody.insertRow();
    rowData.forEach((data, index) => {
        const cell = row.insertCell(index);
        cell.innerHTML = data;
    });

    // Exibe a tabela
    console.log('Exibindo tabela:', table);
    table.style.display = "table";

    // Exibe o botão "Gerar Predição" após exibir a tabela
    const predictionButton = document.getElementById("predictionButton");
    if (predictionButton) {
        predictionButton.style.display = "block";
    } else {
        console.error("Botão Gerar Predição não encontrado.");
    }
}

// Função auxiliar para obter o nome do item com base no índice
function getItemName(index) {
    switch (index) {
        case 1: return "Idade";
        case 2: return "Sexo";
        case 3: return "Colesterol";
        case 4: return "Batimento cardíaco";
        case 5: return "Diabetes";
        case 6: return "Histórico na família";
        case 7: return "Fumante";
        case 8: return "Obesidade";
        case 9: return "Consumo de álcool";
        case 10: return "Problema cardíaco";
        case 11: return "Uso de medicação";
        case 12: return "Nível de estresse";
        case 13: return "Triglicerídeos";
        case 14: return "Atividade física na semana";
        case 15: return "Horas de sono";
        default: return `Item ${index}`;
    }
}

//Gera a predição, coletando os dados da tabela e enviando para o servidor
function generatePrediction() {
    const tableData = collectTableData();
    sendTableDataToServer(tableData);
}

// Criar um array para armazenar os dados da tabela
function collectTableData() {
    const tableData = [];
    for (let i = 1; i <= maxItems; i++) {
        const valueElement = document.getElementById(`newItem${i}`);

        if (valueElement) {
            let value;

            if (valueElement.tagName === 'SELECT') {
                const selectedOption = valueElement.options[valueElement.selectedIndex];
                value = selectedOption ? selectedOption.value : undefined;
            } else {
                value = valueElement.value;
            }

            if (value === undefined) {
                console.error(`Valor indefinido para newItem${i}.`);
                console.error('valueElement:', valueElement);
                return;
            }
            tableData.push(value.trim());
        } else {
            console.error(`Elemento newItem${i} não encontrado ou é nulo.`);
            return;
        }
    }
    return tableData;
}

// Função para enviar dados para o servidor
function sendTableDataToServer(tableData) {
    const formData = new FormData();

    // Mapeia o array de valores para os nomes de itens esperados
    const itemNames = [
        "item1", "item2", "item3", "item4",
        "item5", "item6", "item7", "item8",
        "item9", "item10", "item11", "item12",
        "item13", "item14", "item15", "item16"
    ];

    // Adiciona os dados ao objeto FormData
    tableData.forEach((value, index) => {
        const itemName = itemNames[index];
        formData.append(itemName, value);
    });

    // URL do servidor para POST
    const serverURL = 'http://127.0.0.1:5000/paciente';

    // Enviar a solicitação POST para o servidor
    fetch(serverURL, {
        method: 'POST',
        body: formData
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Resposta do servidor (POST):', data);

        // Após o POST, faça a solicitação GET para obter os dados do ID 1
        getPatientDataById(1);
    })
    .catch((error) => {
        console.error('Erro ao enviar dados para o servidor:', error);
    });
}

// Função para obter dados do paciente por ID
function getPatientDataById(patientId) {
    const getServerURL = `http://127.0.0.1:5000/paciente?id=${patientId}`;
    fetch(getServerURL)
    .then((response) => response.json())
    .then((data) => {
        console.log(`Resposta do servidor (GET) para o ID ${patientId}:`, data);
        const outcome = data.outcome;
        displayOutcome(outcome);
    })
    .catch((error) => {
        console.error(`Erro ao obter dados do paciente com ID ${patientId} do servidor:`, error);
    });
}

// Função para excluir paciente por ID
function deletePatientById(patientId) {
    // URL do servidor para DELETE, incluindo o ID como parâmetro de consulta
    const deleteServerURL = `http://127.0.0.1:5000/paciente_id?id=${patientId}`;

    // Enviar a solicitação DELETE para o servidor
    fetch(deleteServerURL, {
        method: 'DELETE'
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(`Resposta do servidor (DELETE) para o ID ${patientId}:`, data);

    })
    .catch((error) => {
        console.error(`Erro ao excluir paciente com ID ${patientId} do servidor:`, error);
    });
}

// Função para exibir apenas o outcome
function displayOutcome(outcome) {
    // Oculta a tabela
    const table = document.getElementById("resultTable");
    if (table) {
        table.style.display = "none";
    }

    // Exibe apenas o outcome
    const outcomeContainer = document.getElementById("outcomeContainer");
    if (outcomeContainer) {
        outcomeContainer.style.display = "flex";
    }

    const outcomeElement = document.getElementById("outcomeMessage");
    if (outcomeElement) {
        if (outcome === 0) {
            outcomeElement.innerHTML = "Você não tem risco de um infarto cardíaco.";
        } else if (outcome === 1) {
            outcomeElement.innerHTML = "Você tem risco de um infarto cardíaco.";
        } else {
            outcomeElement.innerHTML = "Resultado desconhecido.";
        }

        // Oculta o botão "Gerar Predição"
        predictionButton.style.display = "none";

        // Exibe o botão "Fazer Nova Consulta"
        const refreshButton = document.getElementById("refreshButton");
        if (refreshButton) {
            refreshButton.style.display = "block";
        }

        // Chama a função para excluir o paciente com ID 1 após um intervalo de tempo (por exemplo, 5 segundos)
        setTimeout(() => {
            deletePatientById(1);
        }, 500);
    }
}

// Função para atualizar a página
function refreshPage() {
    location.reload();
}
