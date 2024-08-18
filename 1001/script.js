function copyText() {
    
    var copyText = document.getElementById("myText");

    
    copyText.select();
    copyText.setSelectionRange(0, 99999); 
    navigator.clipboard.writeText(copyText.value)
    .then(() => {
      alert("文本已复制到剪贴板！");
    })
    .catch(err => {
      console.error('复制失败!', err);
    });
}
