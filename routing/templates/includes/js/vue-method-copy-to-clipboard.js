copyToClipboard(inputIdName) {
    const copyText = document.getElementById(inputIdName);
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);

    messageApp.triggerNotification(`Копира текст '${copyText.value}'`);
},