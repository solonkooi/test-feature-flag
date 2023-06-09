# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from . import StationGroupFeatureFlagService_pb2 as StationGroupFeatureFlagService__pb2


class StationGroupFeatureFlagServiceStub(object):
  """
  The Feature Flag Service provides methods to get station groups feature flag values

  Authentication
  ^^^^^^^^^^^^^^
  Please provide a valid ``api_key`` parameter in gRPC service metadata for ``SetFeatureFlag`` and ``DeleteFeatureFlag`` method, otherwise the service will return ``Unauthenticated`` response.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeatureFlag = channel.unary_unary(
        '/featureflag.services.types.stationgroup.StationGroupFeatureFlagService/GetFeatureFlag',
        request_serializer=StationGroupFeatureFlagService__pb2.GetFeatureFlagRequest.SerializeToString,
        response_deserializer=StationGroupFeatureFlagService__pb2.GetFeatureFlagResponse.FromString,
        )
    self.SetFeatureFlag = channel.unary_unary(
        '/featureflag.services.types.stationgroup.StationGroupFeatureFlagService/SetFeatureFlag',
        request_serializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagRequest.SerializeToString,
        response_deserializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagResponse.FromString,
        )
    self.DeleteFeatureFlag = channel.unary_unary(
        '/featureflag.services.types.stationgroup.StationGroupFeatureFlagService/DeleteFeatureFlag',
        request_serializer=StationGroupFeatureFlagService__pb2.DeleteFeatureFlagRequest.SerializeToString,
        response_deserializer=StationGroupFeatureFlagService__pb2.DeleteFeatureFlagResponse.FromString,
        )
    self.SetFeatureFlagForStationGroups = channel.unary_unary(
        '/featureflag.services.types.stationgroup.StationGroupFeatureFlagService/SetFeatureFlagForStationGroups',
        request_serializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagForStationGroupsRequest.SerializeToString,
        response_deserializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagForStationGroupsResponse.FromString,
        )


class StationGroupFeatureFlagServiceServicer(object):
  """
  The Feature Flag Service provides methods to get station groups feature flag values

  Authentication
  ^^^^^^^^^^^^^^
  Please provide a valid ``api_key`` parameter in gRPC service metadata for ``SetFeatureFlag`` and ``DeleteFeatureFlag`` method, otherwise the service will return ``Unauthenticated`` response.
  """

  def GetFeatureFlag(self, request, context):
    """Gets Feature Flag information
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetFeatureFlag(self, request, context):
    """Updates feature flag
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteFeatureFlag(self, request, context):
    """Delete a feature flag for a given application name
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetFeatureFlagForStationGroups(self, request, context):
    """Set feature flag for multiple station groups
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StationGroupFeatureFlagServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeatureFlag': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeatureFlag,
          request_deserializer=StationGroupFeatureFlagService__pb2.GetFeatureFlagRequest.FromString,
          response_serializer=StationGroupFeatureFlagService__pb2.GetFeatureFlagResponse.SerializeToString,
      ),
      'SetFeatureFlag': grpc.unary_unary_rpc_method_handler(
          servicer.SetFeatureFlag,
          request_deserializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagRequest.FromString,
          response_serializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagResponse.SerializeToString,
      ),
      'DeleteFeatureFlag': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteFeatureFlag,
          request_deserializer=StationGroupFeatureFlagService__pb2.DeleteFeatureFlagRequest.FromString,
          response_serializer=StationGroupFeatureFlagService__pb2.DeleteFeatureFlagResponse.SerializeToString,
      ),
      'SetFeatureFlagForStationGroups': grpc.unary_unary_rpc_method_handler(
          servicer.SetFeatureFlagForStationGroups,
          request_deserializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagForStationGroupsRequest.FromString,
          response_serializer=StationGroupFeatureFlagService__pb2.SetFeatureFlagForStationGroupsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'featureflag.services.types.stationgroup.StationGroupFeatureFlagService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
