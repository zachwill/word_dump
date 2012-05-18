$(function(){
  var words = _.shuffle(window._words),
      length = words.length;

  var word = function(){
    var number = Math.floor(Math.random() * length);
    return words[number];
  };

  var create = function(e){
    var random = [word(), word()].join(' ');
    $('.words').html(random);
    return false;
  };

  create();

  $('.new-word').click(create);

});
