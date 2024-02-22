Vamos criar a pasta main, para iniciar o projeto.
A primeira coisa a ser feita será criar a camada CORE da aplicação.

Portanto dentro de src/main vamos criar a pasta chamada core.

    Dentro da pasta core vamos criar uma interface chamada: EmailSenderUseCase com o nome de arquivo: email_sender_use_case.py que será o contrato que define o comportamento da nossa aplicação!


Agora vamos criar as outras camadas.

Criando a camada de applicantion. Ou seja dentro de src/main vamos criar uma pasta chamada application.

    Está camada contém a implementação dos nossos casos de uso, ou seja nela iremos fazer a implementação das interfaces criadas em nossa camada CORE.

    Nossa camada application só irá conhecer a camada CORE.
    E a camada CORE não conhece ninguém!

    Nela iremos criar uma classe chamada: EmailSenderService que irá implementar a interface chamada: EmailSenderUseCase, o arquivo terá o nome de: email_sender_service.py.

Agora vamos criar a camada de adapters.

    Conhecida como interfaces adapters.

    Nesta camada iremos criar outra interface chamada: EmailSenderGateway com o nome de arquivo: email_sender_gateway.py que será o contrato que define o comportamento da porta de envio. Fazendo a conexão da camada externa com as camadas internas.

    Fazendo com que a nossa aplicação dependa dessas interfaces criadas aqui e não do mundo de fora.

    Aqui para o EmailSenderService não depender diretamente da AWS SDK, EMAILGUN ou SENDGRID para que ele não tenha essa dependencia direta dos serviços, criaremos as interfaces aqui.

Agora vamos criar a camada de infra estrutura.

    Essa camada é responsável por interagir com os serviços e estruturas externas.

    No nosso caso é onde vamos implementar a comunicação com nosso AWS SES.

    Portanto vamos criar uma pasta chamada de src/main infra.

    Dentro da pasta infra vamos criar outra pasta com o nome do serviço que será implementado, neste exemplo será o SES.
    Mas poderia ser qualquer outro provedor de serviço de e-mail.

    Dentro da pasta com o nome do serviço neste caso ses vamos criar a classe chamada: SesEmailSender, com o nome de arquivo chamado: ses_email_sender.py

    Está classe recebe a interface da camada adapters, neste caso implementa EmailSenderGateway.


Agora vamos voltar a camada CORE onde ficam nossas regras de negócio. Para criar e personalizar o tratamentos de erros de exceção.

    Portanto iremos criar uma pasta chamada src/main/core/exceptions, e dentro dela iremos criar um arquivo chamado: email_service_exception.py onde criaremos a classe EmailServiceException que implementa a classe Exception.

    Fazendo isso conseguimos modificar a forma que esse tipo de erro ocorre.

Agora vamos criar a camada Controlers.

    Essa camada irá receber as requisições HTTP e vai fazer a chamada de tudo para fazer o disparo de e-mail.
