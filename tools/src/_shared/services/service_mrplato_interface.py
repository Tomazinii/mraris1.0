


from abc import ABC, abstractmethod


class ServiceMrplatoInterface(ABC):

    @abstractmethod
    def prover(self, prover_instance, data, problem: str) -> any:
        raise NotImplementedError
    
    @abstractmethod
    def get_current_status_prover(self, prover_instance, problem):
        raise NotImplementedError
    

    @abstractmethod
    def get_option(self,prover_instance, data, problem) -> any:
        raise NotImplementedError

    
    @abstractmethod
    def get_solution_service(self, prover_instance):
        raise NotImplementedError
    
    @abstractmethod
    def back_state_mrplato(self, prover_instance):
        raise NotImplementedError