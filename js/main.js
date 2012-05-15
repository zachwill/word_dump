$(function(){
  var words = _.shuffle(window._words);

  var create = function(e){
    var random = [words.pop(), words.pop()].join(' ');
    $('.words').html(random);
    return false;
  }

  create();

  $('.new-word').click(create);

});
