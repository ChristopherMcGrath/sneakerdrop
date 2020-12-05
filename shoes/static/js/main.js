

//copy to clipboard

function CopyToClipboard(id)
{
const r = document.createRange();
r.selectNode(document.getElementById(id));
window.getSelection().removeAllRanges();
window.getSelection().addRange(r);
document.execCommand('copy');
window.getSelection().removeAllRanges();
console.log()
}


//tippy

tippy('#myButton', {
    content: 'Copy URL',
    placement: 'top-start',
    arrow: false,
    animation: 'scale',
});


