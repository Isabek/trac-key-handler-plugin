$(window).bind('beforeunload', function(event) {
	var confirmationMessage = "Вы ничего не забыли сохранить?";
	(event || window.event).returnValue = confirmationMessage;
	return confirmationMessage;
});