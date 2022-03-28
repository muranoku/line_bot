// ID名のbtn-helloを指定してボタン要素を取得
var btn= document.getElementById( "btn-hello" );

// イベントハンドラの設定
btn.addEventListener( 
// クリックイベント
"click", 
// イベント後に実行する命令文
function(){
// アラートを表示
alert( btn.textContent )
}
);

