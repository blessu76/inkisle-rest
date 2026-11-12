/* Inkisle: first visit to "/" -> the visitor's browser language (inlined into the root home page only; build_site fills in the list).
   Order: the language the visitor picked on the site (localStorage "ink-lang") > first match in navigator.languages > stay on the English root.
   The match follows ipe_web_kit.languages.resolve: zh-TW/HK/MO/Hant -> zh-Hant, other zh -> none (English), pt* -> pt-BR, in -> id.
   No server redirect: crawlers see "/" as English. */
(function(){
  var S=/*SUPPORTED*/[];
  function pick(tag){
    var p=String(tag||'').toLowerCase().split(/[-_]/).filter(Boolean),c=p[0]==='in'?'id':p[0];
    if(c==='zh'){
      var sc='',rg='';
      for(var k=1;k<p.length;k++){if(!sc&&p[k].length===4)sc=p[k];else if(!rg&&p[k].length===2)rg=p[k];}
      return (sc?sc==='hant':/^(tw|hk|mo)$/.test(rg))?'zh-Hant':'';
    }
    if(c==='pt')c='pt-br';
    for(var j=0;j<S.length;j++)if(S[j].toLowerCase()===c)return S[j];
    return '';
  }
  try{
    if(location.pathname!=='/')return;
    var to='',saved='';
    try{saved=localStorage.getItem('ink-lang')||''}catch(e){}
    if(S.indexOf(saved)>=0)to=saved;
    else{
      var L=(navigator.languages&&navigator.languages.length)?navigator.languages:[navigator.language||''];
      for(var i=0;i<L.length&&!to;i++)to=pick(L[i]);
    }
    if(to&&to!=='en')location.replace('/'+to+'/'+location.search+location.hash);
  }catch(e){}
})();
