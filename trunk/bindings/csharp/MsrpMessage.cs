/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.39
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */


using System;
using System.Runtime.InteropServices;

public class MsrpMessage : IDisposable {
  private HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal MsrpMessage(IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new HandleRef(this, cPtr);
  }

  internal static HandleRef getCPtr(MsrpMessage obj) {
    return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
  }

  ~MsrpMessage() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if(swigCPtr.Handle != IntPtr.Zero && swigCMemOwn) {
        swigCMemOwn = false;
        tinyWRAPPINVOKE.delete_MsrpMessage(swigCPtr);
      }
      swigCPtr = new HandleRef(null, IntPtr.Zero);
      GC.SuppressFinalize(this);
    }
  }

  public MsrpMessage() : this(tinyWRAPPINVOKE.new_MsrpMessage(), true) {
  }

}
