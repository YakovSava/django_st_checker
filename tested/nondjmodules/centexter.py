class Contexter:
	ADMIN_BUTTONS = '''<div class="buttons">
            <button class="btn">Добавить отчёт</button>
            <button class="btn">Дать доступ</button>
            <button class="btn">Удалить компанию</button>
        </div>'''
    COMPANY_CARD = '''<div class="company">
                <div class="company-info">
                    <span class="company-name">ИП Иванов И.И.</span>
                </div>
                <div class="employees">
                    <div class="employee-card">
                        <span class="employee-name">Работник один</span>
                        <div class="employee-credentials">
                            <span class="employee-login-label">Логин:</span>
                            <span class="employee-login">Логин1</span>
                            <br>
                            <span class="employee-password-label">Пароль:</span>
                            <span class="employee-password">пароль1</span>
                        </div>
                    </div>
                    <div class="employee-card">
                        <span class="employee-name">Работник два</span>
                        <div class="employee-credentials">
                            <span class="employee-login-label">Логин:</span>
                            <span class="employee-login">Логин2</span>
                            <br>
                            <span class="employee-password-label">Пароль:</span>
                            <span class="employee-password">пароль2</span>
                        </div>
                    </div>
                </div>
            </div>'''


	def __init__(self):
		pass