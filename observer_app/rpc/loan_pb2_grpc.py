# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import loan_pb2 as loan__pb2


class LoanServiceStub(object):
  """LoanService server
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Healthz = channel.unary_unary(
        '/loan.LoanService/Healthz',
        request_serializer=loan__pb2.HealthzRequest.SerializeToString,
        response_deserializer=loan__pb2.HealthzResponse.FromString,
        )
    self.CreateLoan = channel.unary_unary(
        '/loan.LoanService/CreateLoan',
        request_serializer=loan__pb2.LoanRequest.SerializeToString,
        response_deserializer=loan__pb2.LoanResponse.FromString,
        )
    self.SetWallet = channel.unary_unary(
        '/loan.LoanService/SetWallet',
        request_serializer=loan__pb2.WalletRequest.SerializeToString,
        response_deserializer=loan__pb2.WalletResponse.FromString,
        )
    self.GetLoan = channel.unary_unary(
        '/loan.LoanService/GetLoan',
        request_serializer=loan__pb2.LoanRequest.SerializeToString,
        response_deserializer=loan__pb2.LoanResponse.FromString,
        )
    self.GetLoansList = channel.unary_unary(
        '/loan.LoanService/GetLoansList',
        request_serializer=loan__pb2.LoansListRequest.SerializeToString,
        response_deserializer=loan__pb2.LoansListResponse.FromString,
        )
    self.PaymentsList = channel.unary_unary(
        '/loan.LoanService/PaymentsList',
        request_serializer=loan__pb2.PaymentsListRequest.SerializeToString,
        response_deserializer=loan__pb2.PaymentsListResponse.FromString,
        )
    self.GetSellInfo = channel.unary_unary(
        '/loan.LoanService/GetSellInfo',
        request_serializer=loan__pb2.SellInfoRequest.SerializeToString,
        response_deserializer=loan__pb2.SellInfoResponse.FromString,
        )
    self.GetCurrencies = channel.unary_unary(
        '/loan.LoanService/GetCurrencies',
        request_serializer=loan__pb2.CurrenciesListRequest.SerializeToString,
        response_deserializer=loan__pb2.CurrenciesListResponse.FromString,
        )
    self.CancelLoan = channel.unary_unary(
        '/loan.LoanService/CancelLoan',
        request_serializer=loan__pb2.LoanRequest.SerializeToString,
        response_deserializer=loan__pb2.CancelLoanResponse.FromString,
        )
    self.GetSettings = channel.unary_unary(
        '/loan.LoanService/GetSettings',
        request_serializer=loan__pb2.SettingsRequest.SerializeToString,
        response_deserializer=loan__pb2.SettingsResponse.FromString,
        )
    self.ShowProfData = channel.unary_unary(
        '/loan.LoanService/ShowProfData',
        request_serializer=loan__pb2.ProfRequest.SerializeToString,
        response_deserializer=loan__pb2.ProfResponse.FromString,
        )
    self.GetRatesList = channel.unary_unary(
        '/loan.LoanService/GetRatesList',
        request_serializer=loan__pb2.RatesListRequest.SerializeToString,
        response_deserializer=loan__pb2.RatesListResponse.FromString,
        )
    self.SetSold = channel.unary_unary(
        '/loan.LoanService/SetSold',
        request_serializer=loan__pb2.SetSoldRequest.SerializeToString,
        response_deserializer=loan__pb2.SetSoldResponse.FromString,
        )


class LoanServiceServicer(object):
  """LoanService server
  """

  def Healthz(self, request, context):
    """Healthz is health check. No info returns, only for service availability
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateLoan(self, request, context):
    """Create loan. For creating new borrower, please, invoke GetLoansList at first.
    It's not best way, but let it be so for now.
    Mandatory params are:
    borrower
    body_amount
    pledge_amount
    timeframe
    percent
    pledge_currency
    body_currency
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetWallet(self, request, context):
    """Set body wallet (get wallet address for transfering body amount to borrower after pledge is payed) or
    set pledge return wallet (et wallet address for transfering pledge amount back to borrower after loan is returned)
    Only address, wallet type, loan.id, loan.borrower.id are required
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLoan(self, request, context):
    """Get one loan by id, other params are optionals. With force_update=true will update
    body and pledge wallets balances and debt
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLoansList(self, request, context):
    """List all loans for borrower from request
    If borrower does not exist, it create one whith specified id
    Can be filtered by loan status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PaymentsList(self, request, context):
    """Payments list for specified loan.
    if loan.id specified, then shows payments only for this loan
    update should be set to true for getting new payments from blockchain
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSellInfo(self, request, context):
    """Will be implemented later...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCurrencies(self, request, context):
    """List currencies available in system for loans and pledges
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelLoan(self, request, context):
    """Cancels loan.
    only loan.id required
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSettings(self, request, context):
    """GetSettings returns settings like fee value, rates, wallet types and so on for frontend
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowProfData(self, request, context):
    """ShowProfData returns profiling data for server requests from redis
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRatesList(self, request, context):
    """List rates filtered my RatesListRequest.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSold(self, request, context):
    """SetSold method used by seller for sending sell reports to Loans service
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LoanServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Healthz': grpc.unary_unary_rpc_method_handler(
          servicer.Healthz,
          request_deserializer=loan__pb2.HealthzRequest.FromString,
          response_serializer=loan__pb2.HealthzResponse.SerializeToString,
      ),
      'CreateLoan': grpc.unary_unary_rpc_method_handler(
          servicer.CreateLoan,
          request_deserializer=loan__pb2.LoanRequest.FromString,
          response_serializer=loan__pb2.LoanResponse.SerializeToString,
      ),
      'SetWallet': grpc.unary_unary_rpc_method_handler(
          servicer.SetWallet,
          request_deserializer=loan__pb2.WalletRequest.FromString,
          response_serializer=loan__pb2.WalletResponse.SerializeToString,
      ),
      'GetLoan': grpc.unary_unary_rpc_method_handler(
          servicer.GetLoan,
          request_deserializer=loan__pb2.LoanRequest.FromString,
          response_serializer=loan__pb2.LoanResponse.SerializeToString,
      ),
      'GetLoansList': grpc.unary_unary_rpc_method_handler(
          servicer.GetLoansList,
          request_deserializer=loan__pb2.LoansListRequest.FromString,
          response_serializer=loan__pb2.LoansListResponse.SerializeToString,
      ),
      'PaymentsList': grpc.unary_unary_rpc_method_handler(
          servicer.PaymentsList,
          request_deserializer=loan__pb2.PaymentsListRequest.FromString,
          response_serializer=loan__pb2.PaymentsListResponse.SerializeToString,
      ),
      'GetSellInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetSellInfo,
          request_deserializer=loan__pb2.SellInfoRequest.FromString,
          response_serializer=loan__pb2.SellInfoResponse.SerializeToString,
      ),
      'GetCurrencies': grpc.unary_unary_rpc_method_handler(
          servicer.GetCurrencies,
          request_deserializer=loan__pb2.CurrenciesListRequest.FromString,
          response_serializer=loan__pb2.CurrenciesListResponse.SerializeToString,
      ),
      'CancelLoan': grpc.unary_unary_rpc_method_handler(
          servicer.CancelLoan,
          request_deserializer=loan__pb2.LoanRequest.FromString,
          response_serializer=loan__pb2.CancelLoanResponse.SerializeToString,
      ),
      'GetSettings': grpc.unary_unary_rpc_method_handler(
          servicer.GetSettings,
          request_deserializer=loan__pb2.SettingsRequest.FromString,
          response_serializer=loan__pb2.SettingsResponse.SerializeToString,
      ),
      'ShowProfData': grpc.unary_unary_rpc_method_handler(
          servicer.ShowProfData,
          request_deserializer=loan__pb2.ProfRequest.FromString,
          response_serializer=loan__pb2.ProfResponse.SerializeToString,
      ),
      'GetRatesList': grpc.unary_unary_rpc_method_handler(
          servicer.GetRatesList,
          request_deserializer=loan__pb2.RatesListRequest.FromString,
          response_serializer=loan__pb2.RatesListResponse.SerializeToString,
      ),
      'SetSold': grpc.unary_unary_rpc_method_handler(
          servicer.SetSold,
          request_deserializer=loan__pb2.SetSoldRequest.FromString,
          response_serializer=loan__pb2.SetSoldResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'loan.LoanService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
