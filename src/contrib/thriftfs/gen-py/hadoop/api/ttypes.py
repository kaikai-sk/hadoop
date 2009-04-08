#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class DatanodeReportType:
  ALL_DATANODES = 1
  LIVE_DATANODES = 2
  DEAD_DATANODES = 3

class DatanodeState:
  NORMAL_STATE = 1
  DECOMMISSION_INPROGRESS = 2
  DECOMMISSIONED = 3

class DatanodeInfo:
  """
  Information and state of a data node.
  
  Modelled after org.apache.hadoop.hdfs.protocol.DatanodeInfo
  
  Attributes:
   - name: HDFS name of the datanode (equals to <host>:<datanode port>)
   - storageID: Unique ID within a HDFS cluster
   - host: Host name of the Thrift server socket.
   - thriftPort: Port number of the Thrift server socket, or UNKNOWN_THRIFT_PORT
  if the Thrift port for this datanode is not known.
   - capacity: Raw capacity of the data node (in bytes).
   - dfsUsed: Space used by the data node (in bytes).
   - remaining: Raw free space in the data node (in bytes).
   - xceiverCount: Number of active connections to the data node.
   - state: State of this data node.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'storageID', None, None, ), # 2
    (3, TType.STRING, 'host', None, None, ), # 3
    (4, TType.I32, 'thriftPort', None, None, ), # 4
    (5, TType.I64, 'capacity', None, None, ), # 5
    (6, TType.I64, 'dfsUsed', None, None, ), # 6
    (7, TType.I64, 'remaining', None, None, ), # 7
    (8, TType.I32, 'xceiverCount', None, None, ), # 8
    (9, TType.I32, 'state', None, None, ), # 9
  )

  def __init__(self, name=None, storageID=None, host=None, thriftPort=None, capacity=None, dfsUsed=None, remaining=None, xceiverCount=None, state=None,):
    self.name = name
    self.storageID = storageID
    self.host = host
    self.thriftPort = thriftPort
    self.capacity = capacity
    self.dfsUsed = dfsUsed
    self.remaining = remaining
    self.xceiverCount = xceiverCount
    self.state = state

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.storageID = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.host = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.thriftPort = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.capacity = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.dfsUsed = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.remaining = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.xceiverCount = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.state = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('DatanodeInfo')
    if self.name != None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.storageID != None:
      oprot.writeFieldBegin('storageID', TType.STRING, 2)
      oprot.writeString(self.storageID)
      oprot.writeFieldEnd()
    if self.host != None:
      oprot.writeFieldBegin('host', TType.STRING, 3)
      oprot.writeString(self.host)
      oprot.writeFieldEnd()
    if self.thriftPort != None:
      oprot.writeFieldBegin('thriftPort', TType.I32, 4)
      oprot.writeI32(self.thriftPort)
      oprot.writeFieldEnd()
    if self.capacity != None:
      oprot.writeFieldBegin('capacity', TType.I64, 5)
      oprot.writeI64(self.capacity)
      oprot.writeFieldEnd()
    if self.dfsUsed != None:
      oprot.writeFieldBegin('dfsUsed', TType.I64, 6)
      oprot.writeI64(self.dfsUsed)
      oprot.writeFieldEnd()
    if self.remaining != None:
      oprot.writeFieldBegin('remaining', TType.I64, 7)
      oprot.writeI64(self.remaining)
      oprot.writeFieldEnd()
    if self.xceiverCount != None:
      oprot.writeFieldBegin('xceiverCount', TType.I32, 8)
      oprot.writeI32(self.xceiverCount)
      oprot.writeFieldEnd()
    if self.state != None:
      oprot.writeFieldBegin('state', TType.I32, 9)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Block:
  """
  Representation of a file block in HDFS
  
  Modelled after org.apache.hadoop.hdfs.protocol.LocatedBlock
  
  Attributes:
   - blockId: Block ID (unique among all blocks in a filesystem).
   - path: Path of the file which this block belongs to.
   - numBytes: Length of this block.
   - genStamp: Generational stamp of this block.
   - nodes: List of data nodes with copies  of this block.
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'blockId', None, None, ), # 1
    (2, TType.STRING, 'path', None, None, ), # 2
    (3, TType.I64, 'numBytes', None, None, ), # 3
    (4, TType.I64, 'genStamp', None, None, ), # 4
    (5, TType.LIST, 'nodes', (TType.STRUCT,(DatanodeInfo, DatanodeInfo.thrift_spec)), None, ), # 5
  )

  def __init__(self, blockId=None, path=None, numBytes=None, genStamp=None, nodes=None,):
    self.blockId = blockId
    self.path = path
    self.numBytes = numBytes
    self.genStamp = genStamp
    self.nodes = nodes

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.blockId = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.path = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.numBytes = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.genStamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.nodes = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = DatanodeInfo()
            _elem5.read(iprot)
            self.nodes.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Block')
    if self.blockId != None:
      oprot.writeFieldBegin('blockId', TType.I64, 1)
      oprot.writeI64(self.blockId)
      oprot.writeFieldEnd()
    if self.path != None:
      oprot.writeFieldBegin('path', TType.STRING, 2)
      oprot.writeString(self.path)
      oprot.writeFieldEnd()
    if self.numBytes != None:
      oprot.writeFieldBegin('numBytes', TType.I64, 3)
      oprot.writeI64(self.numBytes)
      oprot.writeFieldEnd()
    if self.genStamp != None:
      oprot.writeFieldBegin('genStamp', TType.I64, 4)
      oprot.writeI64(self.genStamp)
      oprot.writeFieldEnd()
    if self.nodes != None:
      oprot.writeFieldBegin('nodes', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.nodes))
      for iter6 in self.nodes:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Stat:
  """
  Information about a path in HDFS.
  
  Modelled after org.apache.hadoop.fs.ContentSummary and
                 org.apache.hadoop.fs.FileStatus
  
  Attributes:
   - path: The path.
   - isDir: True:  The path represents a file.
  False: The path represents a directory.
   - atime: Access time (milliseconds since 1970-01-01 00:00 UTC).
   - mtime: Modification time (milliseconds since 1970-01-01 00:00 UTC).
   - perms: Access permissions
   - owner: Owner
   - group: Group
   - fileCount: Number of files in this directory
   - directoryCount: Number of directories in this directory
   - quota: Quota for this directory (in bytes).
   - spaceConsumed: Space consumed in disk (in bytes).
   - spaceQuota: Quota consumed in disk (in bytes).
   - length: Length (in bytes).
   - blockSize: Block size (in bytes).
   - replication: Replication factor.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'path', None, None, ), # 1
    (2, TType.BOOL, 'isDir', None, None, ), # 2
    (3, TType.I64, 'atime', None, None, ), # 3
    (4, TType.I64, 'mtime', None, None, ), # 4
    (5, TType.I16, 'perms', None, None, ), # 5
    (6, TType.STRING, 'owner', None, None, ), # 6
    (7, TType.STRING, 'group', None, None, ), # 7
    (8, TType.I64, 'fileCount', None, None, ), # 8
    (9, TType.I64, 'directoryCount', None, None, ), # 9
    (10, TType.I64, 'quota', None, None, ), # 10
    (11, TType.I64, 'spaceConsumed', None, None, ), # 11
    (12, TType.I64, 'spaceQuota', None, None, ), # 12
    (13, TType.I64, 'length', None, None, ), # 13
    (14, TType.I64, 'blockSize', None, None, ), # 14
    (15, TType.I16, 'replication', None, None, ), # 15
  )

  def __init__(self, path=None, isDir=None, atime=None, mtime=None, perms=None, owner=None, group=None, fileCount=None, directoryCount=None, quota=None, spaceConsumed=None, spaceQuota=None, length=None, blockSize=None, replication=None,):
    self.path = path
    self.isDir = isDir
    self.atime = atime
    self.mtime = mtime
    self.perms = perms
    self.owner = owner
    self.group = group
    self.fileCount = fileCount
    self.directoryCount = directoryCount
    self.quota = quota
    self.spaceConsumed = spaceConsumed
    self.spaceQuota = spaceQuota
    self.length = length
    self.blockSize = blockSize
    self.replication = replication

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.path = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.isDir = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.atime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.mtime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I16:
          self.perms = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.owner = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.group = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.fileCount = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.directoryCount = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I64:
          self.quota = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I64:
          self.spaceConsumed = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I64:
          self.spaceQuota = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.I64:
          self.length = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.I64:
          self.blockSize = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.I16:
          self.replication = iprot.readI16();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Stat')
    if self.path != None:
      oprot.writeFieldBegin('path', TType.STRING, 1)
      oprot.writeString(self.path)
      oprot.writeFieldEnd()
    if self.isDir != None:
      oprot.writeFieldBegin('isDir', TType.BOOL, 2)
      oprot.writeBool(self.isDir)
      oprot.writeFieldEnd()
    if self.atime != None:
      oprot.writeFieldBegin('atime', TType.I64, 3)
      oprot.writeI64(self.atime)
      oprot.writeFieldEnd()
    if self.mtime != None:
      oprot.writeFieldBegin('mtime', TType.I64, 4)
      oprot.writeI64(self.mtime)
      oprot.writeFieldEnd()
    if self.perms != None:
      oprot.writeFieldBegin('perms', TType.I16, 5)
      oprot.writeI16(self.perms)
      oprot.writeFieldEnd()
    if self.owner != None:
      oprot.writeFieldBegin('owner', TType.STRING, 6)
      oprot.writeString(self.owner)
      oprot.writeFieldEnd()
    if self.group != None:
      oprot.writeFieldBegin('group', TType.STRING, 7)
      oprot.writeString(self.group)
      oprot.writeFieldEnd()
    if self.fileCount != None:
      oprot.writeFieldBegin('fileCount', TType.I64, 8)
      oprot.writeI64(self.fileCount)
      oprot.writeFieldEnd()
    if self.directoryCount != None:
      oprot.writeFieldBegin('directoryCount', TType.I64, 9)
      oprot.writeI64(self.directoryCount)
      oprot.writeFieldEnd()
    if self.quota != None:
      oprot.writeFieldBegin('quota', TType.I64, 10)
      oprot.writeI64(self.quota)
      oprot.writeFieldEnd()
    if self.spaceConsumed != None:
      oprot.writeFieldBegin('spaceConsumed', TType.I64, 11)
      oprot.writeI64(self.spaceConsumed)
      oprot.writeFieldEnd()
    if self.spaceQuota != None:
      oprot.writeFieldBegin('spaceQuota', TType.I64, 12)
      oprot.writeI64(self.spaceQuota)
      oprot.writeFieldEnd()
    if self.length != None:
      oprot.writeFieldBegin('length', TType.I64, 13)
      oprot.writeI64(self.length)
      oprot.writeFieldEnd()
    if self.blockSize != None:
      oprot.writeFieldBegin('blockSize', TType.I64, 14)
      oprot.writeI64(self.blockSize)
      oprot.writeFieldEnd()
    if self.replication != None:
      oprot.writeFieldBegin('replication', TType.I16, 15)
      oprot.writeI16(self.replication)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class IOException(Exception):
  """
  Generic I/O error
  
  Attributes:
   - msg: Error message.
   - stack: Textual representation of the call stack.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
    (2, TType.STRING, 'stack', None, None, ), # 2
  )

  def __init__(self, msg=None, stack=None,):
    self.msg = msg
    self.stack = stack

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stack = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IOException')
    if self.msg != None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg)
      oprot.writeFieldEnd()
    if self.stack != None:
      oprot.writeFieldBegin('stack', TType.STRING, 2)
      oprot.writeString(self.stack)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QuotaException(Exception):
  """
  Quota-related error
  
  Attributes:
   - msg: Error message.
   - stack: Textual representation of the call stack.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
    (2, TType.STRING, 'stack', None, None, ), # 2
  )

  def __init__(self, msg=None, stack=None,):
    self.msg = msg
    self.stack = stack

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stack = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QuotaException')
    if self.msg != None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg)
      oprot.writeFieldEnd()
    if self.stack != None:
      oprot.writeFieldBegin('stack', TType.STRING, 2)
      oprot.writeString(self.stack)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BlockData:
  """
  Encapsulates a block data transfer with its CRC
  
  Attributes:
   - crc: CRC32 of the data being transfered
   - length: Length of the data being transfered
   - data: The data itsef
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'crc', None, None, ), # 1
    (2, TType.I32, 'length', None, None, ), # 2
    (3, TType.STRING, 'data', None, None, ), # 3
  )

  def __init__(self, crc=None, length=None, data=None,):
    self.crc = crc
    self.length = length
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.crc = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.length = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.data = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BlockData')
    if self.crc != None:
      oprot.writeFieldBegin('crc', TType.I32, 1)
      oprot.writeI32(self.crc)
      oprot.writeFieldEnd()
    if self.length != None:
      oprot.writeFieldBegin('length', TType.I32, 2)
      oprot.writeI32(self.length)
      oprot.writeFieldEnd()
    if self.data != None:
      oprot.writeFieldBegin('data', TType.STRING, 3)
      oprot.writeString(self.data)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
