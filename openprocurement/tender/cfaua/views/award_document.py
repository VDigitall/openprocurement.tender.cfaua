# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openua.views.award_document import TenderUaAwardDocumentResource as BaseResource


@optendersresource(name='closeFrameworkAgreementUA:Tender Award Documents',
                   collection_path='/tenders/{tender_id}/awards/{award_id}/documents',
                   path='/tenders/{tender_id}/awards/{award_id}/documents/{document_id}',
                   procurementMethodType='closeFrameworkAgreementUA',
                   description="Tender award documents")
class TenderAwardDocumentResource(BaseResource):
    """ Tender Award Document """
