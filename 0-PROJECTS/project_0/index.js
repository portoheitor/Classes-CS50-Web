function luckySearch() {
    const form = document.querySelector('.search-form');
    form.action = 'https://www.google.com/search';
    const input = document.querySelector('input[name="q"]');
    const luckyParam = document.createElement('input');
    luckyParam.type = 'hidden';
    luckyParam.name = 'btnI';
    luckyParam.value = 'I';
    form.appendChild(luckyParam);
    form.submit();
}