from django.db import models

#criar tabela para manutenção realizada
class ManutecaoRealizada():
    #registro de manutencoes realizadas que devem ser compostas por profissional responsavel, hora da realizacao, orçamento e obs.
    pass

#criar tabela para solicitacao de manutencao
class SolicitacaoManutencao():
    #para moradores solicitarem manutenções e funcionarios solicitam manutencoes
    #aqui os funcionarios que vao analisar se a solicitacao foi aceita ou nao
    pass

#criar tabela para lista de manutencao
class ManutecaoPendente():
    #controle que ficará até a manutencao ser realizada
    pass

#criar tabela para manutencoes periodicas
class ManutencaoPeriodicas():
    #exclusivo para manutencoes que devem ser feitas de tempos em tempos como piscinal, bombas, jardinagem e eletrica.
    pass

#criar tabela para manutecao agendada
class ManutencaoAgendada():
    #exclusivo para agendar manutencao futura, vai ser notificador aos profissionais que devem realizar essa manutenção
    pass
