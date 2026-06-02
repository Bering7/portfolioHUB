function copiarEmail() {
    // Coloque o seu e-mail real aqui entre as aspas
    const meuEmail = "riquemoura.bering@gmail.com"; 
    
    navigator.clipboard.writeText(meuEmail).then(() => {
        const textoElement = document.getElementById("texto-email");
        const iconeElement = document.querySelector("#btn-email .contato-icone");
        
        // Salva o texto original para voltar depois
        const textoOriginal = textoElement.innerText;
        const iconeOriginal = iconeElement.innerText;
        
        // Altera o botão para avisar que copiou
        textoElement.innerText = "Copiado!";
        iconeElement.innerText = "✅";
        document.getElementById("btn-email").style.borderColor = "#27ae60";
        textoElement.style.color = "#27ae60";
        
        // Depois de 2.5 segundos, volta tudo ao normal
        setTimeout(() => {
            textoElement.innerText = textoOriginal;
            iconeElement.innerText = iconeOriginal;
            document.getElementById("btn-email").style.borderColor = "";
            textoElement.style.color = "";
        }, 2500);
    }).catch(err => {
        console.error("Erro ao copiar e-mail: ", err);
    });
}